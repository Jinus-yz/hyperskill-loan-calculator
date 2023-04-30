import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

if args.type is None or (args.type != "annuity" and args.type != "diff"):
    print("Incorrect parameters")
    exit()

calc_type = str(args.type)
payment = int(args.payment or 0)
principal = int(args.principal or 0)
periods = int(args.periods or 0)
interest = float(args.interest or 0)

if interest <= 0:
    print("Incorrect parameters")
    exit()

i = interest / 1200

if calc_type == "diff":
    if args.payment is not None or principal <= 0 or periods <= 0:
        print("Incorrect parameters")
        exit()

    total = 0

    for m in range(periods):
        payment = math.ceil(principal / periods + (i * (principal - (principal * m / periods))))
        total += payment
        print(f"Month {m + 1}: payment is {payment}")

    overpayment = total - principal

    if overpayment > 0:
        print(f"Overpayment = {overpayment}")
elif calc_type == "annuity":
    if args.payment is not None and args.principal is not None and args.periods is not None:
        print("Incorrect parameters")
        exit()
    elif args.payment is None:
        if principal <= 0 or periods <= 0:
            print("Incorrect parameters")
            exit()

        payment = math.ceil(principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
        overpayment = (payment * periods) - principal

        print(f"Your annuity payment = {payment}!")

        if overpayment > 0:
            print(f"Overpayment = {overpayment}")
    elif args.principal is None:
        if payment <= 0 or periods <= 0:
            print("Incorrect parameters")
            exit()

        principal = math.floor(payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
        overpayment = (payment * periods) - principal

        print(f"Your loan principal = {principal}!")

        if overpayment > 0:
            print(f"Overpayment = {overpayment}")
    elif args.periods is None:
        if payment <= 0 or principal <= 0:
            print("Incorrect parameters")
            exit()

        x = payment / (payment - i * principal)
        periods = math.ceil(math.log(x, 1 + i))

        years = periods // 12
        months = (periods % 12) if years > 0 else 0
        period = []

        if years > 0:
            period.append(f"{years} year{'s' if years > 1 else ''}")

        if months > 0:
            period.append(f"{months} month{'s' if months > 1 else ''}")

        if len(period) == 0:
            period.append("1 month")

        periods_str = ' '.join(period)
        overpayment = (payment * periods) - principal

        print(f"It will take {periods_str} to repay this loan!")

        if overpayment > 0:
            print(f"Overpayment = {overpayment}")
