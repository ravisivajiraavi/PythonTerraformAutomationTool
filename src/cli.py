import click
from terraform_wrapper import terraform_init, terraform_plan, terraform_apply, terraform_destroy

@click.group()
def cli():
    pass

@cli.command()
def init():
    """Initialize Terraform configuration"""
    terraform_init()

@cli.command()
def plan():
    """Run Terraform plan"""
    terraform_plan()

@cli.command()
def apply():
    """Apply Terraform configuration"""
    terraform_apply()

@cli.command()
def destroy():
    """Destroy Terraform-managed infrastructure"""
    terraform_destroy()

if __name__ == "__main__":
    cli()
