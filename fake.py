from profile import Profile
from product.company import Company
from product.product import Product
from product.purchase import Purchase

from finance.accounttransfer import AccountTransfer
from finance.account import Account
from finance.bank import Bank

from terminationcondition import TimedRun, CountRun

import sys
import argparse
import time

from kafka import kafka_send, kafka_flush

types = {
    "bank": Bank,
    "company": Company,
    "product": Product,
    "account": Account,
    "accounttransfer": AccountTransfer,
    "purchase": Purchase,
    "profile": Profile
}

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="type of object to generate", type=str)
    parser.add_argument("--stream", help="stream to produce messages on", type=str)
    parser.add_argument("-n", help="How many to generate", default=None, type=int)
    parser.add_argument("--ms", help="Generate records for this many milliseconds", default=None, type=int)
    parser.add_argument("--topic", help="Kafka topic to send to", default=None)
    parser.add_argument("--dryrun", help="If set, kafka messages won't be sent", action='store_true')
    return parser

def usage(parser):
    parser.print_help()
    sys.exit(1)

def generate(constructor, topic, termination_condition, dry_run=False):
    count = 0

    while True:
        count = count + 1
        thing = constructor.create()
        print(thing)

        if not dry_run:
            kafka_send(topic, thing)

        termination_condition.ran(thing)
        if termination_condition.finished(): 
            break

    if not dry_run:
        print("Flushing kafka...")
        kafka_flush()
    
    print("Dry-run %s" % dry_run)
    return count


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args.type:
        usage(parser)

    if not args.n and not args.ms:
        # Default is to just produce 1.
        args.n = 1

    try:
        constructor = types[args.type.lower().strip()]
    except KeyError:
        print("Unrecognized type %s" % args.type)
        print("Options are:\n   %s" % "\n   ".join(types.keys()))
        usage(parser)

    tc = None

    # Set a termination condition
    if args.ms is not None: tc = TimedRun(args.ms)
    else: tc = CountRun(args.n)

    if args.n and args.ms:
        print("You may only specify n or ms, one or the other, not both")
        usage(parser)

    if not args.topic:
        args.topic = args.type.lower().strip()

    generate(constructor, args.topic, tc, args.dryrun)

if __name__== "__main__":
  main()