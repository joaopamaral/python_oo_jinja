from jinja2 import Environment, FileSystemLoader


class InfraJinja:
    def __init__(self, name, cloud):
        self.name = name
        self.cloud = cloud


if __name__ == '__main__':
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('infra.template')

    output = template.render(infras=[
        InfraJinja('infra1', 'aws'),
        InfraJinja('infra2', 'gcp'),
        InfraJinja('infra3', 'azure')
    ])
    print(output)

    with open("output/mytf.tf", "w") as fh:
        fh.write(output)