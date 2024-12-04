import argparse
from data import request_power_outage_data


def main(args: argparse.Namespace) -> None:
    power_outage_data = request_power_outage_data(args.address)
    if power_outage_data.current.hasQueue == 'yes':
        today = power_outage_data.graphs.today
        if today is not None:
            for hour in today.hoursList:
                print(hour)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--address', help='Power outage schedule address', type=str)
    args = parser.parse_args()
    main(args)