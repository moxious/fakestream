from profile import Profile
from product.company import Company
from product.product import Product
from product.purchase import Purchase

from finance.accounttransfer import AccountTransfer
from finance.account import Account
from finance.bank import Bank
from streamentry import TemplateStreamEntry
from terminationcondition import TimedRun, CountRun
from domain import Domain

import sys
import argparse
import time
import json

from kafka import kafka_send, kafka_flush

types = {
    "bank": Bank,
    "company": Company,
    "product": Product,
    "account": Account,
    "accounttransfer": AccountTransfer,
    "purchase": Purchase,
    "profile": Profile,
    "customer": Profile
}

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="type of object to generate", default=None, type=str)
    parser.add_argument("--stream", help="stream to produce messages on", type=str)
    parser.add_argument("-n", help="How many to generate", default=None, type=int)
    parser.add_argument("--ms", help="Generate records for this many milliseconds", default=None, type=int)
    parser.add_argument("--topic", help="Kafka topic to send to", default=None)
    parser.add_argument("--mps", help="Messages per second to send", default=1, type=float)
    parser.add_argument("--dryrun", help="If set, kafka messages won't be sent", action='store_true')
    parser.add_argument("--template", help="Template JSON file", default=None, type=str)
    parser.add_argument("--domain", help="Domain JSON file", default="domain.json")
    return parser

def usage(parser):
    parser.print_help()
    sys.exit(1)

def generate(constructor, termination_condition, args):
    count = 0

    topic = args.topic
    dry_run = args.dryrun

    if not topic: 
        raise Exception("Must provide topic")
    
    sleep_time_sec = 1 / args.mps

    while True:
        count = count + 1
        thing = constructor()
        print(thing)

        if not dry_run:
            kafka_send(topic, thing)

        termination_condition.ran(thing)
        if termination_condition.finished(): 
            break
        
        time.sleep(sleep_time_sec)

    if not dry_run:
        print("Flushing kafka...")
        kafka_flush()
    
    return count

def create_constructor_from_template(template_file):
    with open(template_file) as json_file: 
        data = json.load(json_file)
    
    return lambda: TemplateStreamEntry.create(data)

def get_constructor(args, parser):
    if not args.type and not args.template:
        print("You must specify either --type or --template")
        usage(parser)

    if args.type:
        try:
            object_type = types[args.type.lower().strip()]
            return lambda: object_type.create()
        except KeyError:
            print("Unrecognized type %s" % args.type)
            print("Options are:\n   %s" % "\n   ".join(types.keys()))
            usage(parser)
    
    return create_constructor_from_template(args.template)

def stats(tc):
    elapsed = tc.elapsed()
    count = tc.get_count()
    ms_per_msg = elapsed / count
    msg_per_sec = count / (elapsed / 1000)
    print("Production stats:")
    print("   %d messages in" % count)
    print("   %d millseconds" % elapsed)
    print("   %f milliseconds/message, or" % ms_per_msg)
    print("   %f messages/sec actual" % msg_per_sec)

def finish_and_exit(tc, message="All Done", exit_code=0):
    print(message)
    stats(tc)
    sys.exit(exit_code)

def main():
    parser = create_parser()
    args = parser.parse_args()

    constructor = get_constructor(args, parser)

    if not args.n and not args.ms:
        # Default is to just produce 1.
        args.n = 1

    tc = None

    # Set a termination condition
    if args.ms is not None: tc = TimedRun(args.ms)
    else: tc = CountRun(args.n)

    if args.n and args.ms:
        print("You may only specify n or ms, one or the other, not both")
        usage(parser)

    if not args.topic:
        args.topic = args.type.lower().strip()

    domain = Domain(args.domain)
    try:
        generate(constructor, tc, args)
    except KeyboardInterrupt:
        finish_and_exit(tc, "\n\nInterrupted.  Exiting", 1)

    finish_and_exit(tc)

if __name__== "__main__":
  main()