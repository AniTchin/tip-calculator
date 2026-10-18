"""Tip Calculator - პატარა CLI პროგრამა ჩაის ფულის გამოსათვლელად."""
import sys


def calculate_tip(bill: float, percent: float = 10) -> float:
    """აბრუნებს ჩაის ფულს ანგარიშის და პროცენტის მიხედვით."""
    return round(bill * percent / 100, 2)


def main() -> None:
    if len(sys.argv) < 2:
        print("გამოყენება: python tip.py <თანხა> [პროცენტი]")
        sys.exit(1)
    bill = float(sys.argv[1])
    percent = float(sys.argv[2]) if len(sys.argv) > 2 else 10
    tip = calculate_tip(bill, percent)
    print(f"ჩაი: {tip} ₾ | ჯამი: {round(bill + tip, 2)} ₾")


if __name__ == "__main__":
    main()
