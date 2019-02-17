import click
import MedianCalculator as mCalc
import CSVreformatter as csv

@click.command()

@click.option('--date', required = True, nargs = 1,
              help="Please format the input in following format YYYY-MM-DD")
@click.option('--time', required = True, nargs = 1,
              help="Please format the input in following format x-y")
@click.option('--city', default='Helsinki', required=False, nargs = 1,
              help="Default is Helsinki but it can be changed by adding a third parameter")
@click.argument('out', type= click.File('w'), default='mediantimes.csv', required=False)


def cli(date, time, city, out):
    """This is a command line application for Wolt Coding Task 2019 - Pickup times.\n
         The median output is archived in mediantimes.csv.\n
         By providing a fourth parameter in the form of file name,\n
         this default can be changed.\n
         The program always overwrites the previous data, so by changing the filename,\n
         it's possible to save the data easily."""
    medianPickup = []
    locations = csv.Formatting().returnLocs()
    for location in locations:
        data = mCalc.Select(location, date, time[:2], time[-2:])
        medianPickup.append((location, data.getPickupTime()))
    click.echo("Median pickup times in the city of " + city + ",\norganized by the ID of the restaurant.")
    click.echo("location_id, median_pickup_time")
    click.echo("location_id,median_pickup_time", file=out)
    for median in medianPickup:
        
        click.echo(click.style(str(median[0]) + "," + str(median[1]), fg = 'blue'))
        click.echo(str(median[0]) + "," + str(median[1]), file=out)

    
