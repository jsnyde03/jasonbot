import logging
import os
import argparse
import signal
import sys
from pathlib import Path
import asyncio
import discord
import config, discord_task, restock_monitor, nonshopify_monitor, shopify_monitor, proxies
import JasonBot


def init(monitor):
    logging.basicConfig(format=config.LOG_FORMAT.format(monitor), filename=config.LOG_FILE, level=logging.INFO)

    if os.path.isfile(config.PID_FILES[monitor]):
        logging.info("JasonBot is already running")
        sys.exit("JasonBot is already running")

    pid = os.getpid()
    logging.info("Start with PID: {}".format(pid))
    with open(config.PID_FILES[monitor], 'w') as f:
        f.write("{}".format(pid))


def check(args):
    init(args.monitor)
    try:
        if args.monitor == "restock":
            restock_monitor.RestockMonitor().check()
        elif args.monitor == "nonshopify":
            nonshopify_monitor.NonShopifyMonitor().check()
        elif args.monitor == "shopify":
            shopify_monitor.ShopifyMonitor(proxies.get_proxies()).check()
        else:
            raise Exception("Invalid monitor name")
    except Exception as e:
        logging.exception(e)
    finally:
        os.remove(config.PID_FILES[args.monitor])


def start(args):
    init(args.monitor)
    daemon = discord_daemon.DiscordDaemon()
    daemon.run(config.BOT_TOKEN)

def stop(args):
    if not os.path.isfile(config.PID_FILES[args.monitor]):
        sys.exit("JasonBot PID_FILE not found")
    pid = int(Path(config.PID_FILES[args.monitor]).read_text().strip())
    os.kill(pid, signal.SIGTERM)
    os.remove(config.PID_FILES[args.monitor])

def restart(args):
    stop(args)
    start(args)

def parse_args():
    parser = argparse.ArgumentParser(prog='JasonBot')
    sp = parser.add_subparsers()
    sp_start = sp.add_parser('start', help='Starts %(prog)s daemon')
    sp_start.set_defaults(func=start)
    sp_stop = sp.add_parser('stop', help='Stops %(prog)s daemon')
    sp_stop.set_defaults(func=stop)
    sp_restart = sp.add_parser('restart', help='Restarts %(prog)s daemon')
    sp_restart.set_defaults(func=restart)
    sp_check = sp.add_parser('check', help='Run one check and exit')
    sp_check.add_argument("monitor")
    sp_check.set_defaults(func=check)
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        args.func(args)
    except AttributeError:
        print("usage: JasonBot [-h] {start,stop,restart,check} ...")
        print("JasonBot: error: invalid choice: '' (choose from 'start', 'stop', 'restart', 'check')")
    except KeyboardInterrupt:
        stop(args)

if __name__ == "__main__":
    main()


