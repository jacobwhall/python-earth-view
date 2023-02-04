import click

from .main import EarthViewImage, random_image_id

@click.command()
@click.argument("path",
                type=click.Path())
@click.option("-i",
              "--id",
              default=random_image_id(),
              help="ID of desired Earth View image.")
@click.option("--overwrite",
              is_flag=True)
def get_image(path, id, overwrite):
    EarthViewImage(id).save(path, overwrite)

if __name__ == "__main__":
    get_image()
