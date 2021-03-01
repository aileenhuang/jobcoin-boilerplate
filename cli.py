#!/usr/bin/env python
import uuid
import sys

import click

from jobcoin import jobcoin


@click.command()
def main(args=None):
    print('Welcome to the Jobcoin mixer!\n')
    while True:
        addresses = click.prompt(
            'Please enter a comma-separated list of new, unused Jobcoin '
            'addresses where your mixed Jobcoins will be sent.',
            prompt_suffix='\n[blank to quit] > ',
            default='',
            show_default=False)
        if addresses.strip() == '':
            sys.exit(0)
        deposit_address = uuid.uuid4().hex
        click.echo(
            '\nYou may now send Jobcoins to address {deposit_address}. They '
            'will be mixed and sent to your destination addresses.\n'
              .format(deposit_address=deposit_address))

        source_address = click.prompt(
            "Please enter your source address.",
            prompt_suffix="\n[blank to quit] >",
            default="",
            show_default=False)
        if source_address.strip() == "":
            sys.exit(0)

        amount = click.prompt(
            "Please enter your transaction amount.",
            prompt_suffix="\n[blank to quit] >",
            default="",
            show_default=False)
        
        if amount.strip() == "":
            sys.exit(0)

        conf = click.prompt(
            "Sending {} Jobcoin from {} to {}. Are you sure you want to proceed with this transaction? [Y/n]".format(amount, source_address, deposit_address),
            prompt_suffix="\n[blank to quit] >",
            default="",
            show_default=False)
        
        if conf not in ["Y", "n"]:
            sys.exit(0)

        # Run jobcoin here


if __name__ == '__main__':
    sys.exit(main())

