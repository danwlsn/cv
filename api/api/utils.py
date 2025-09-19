from datetime import date as Date


def date_between_dates(date: Date, start: Date, end: Date | None) -> bool:
    if end is None:
        return date >= start
    return start <= date <= end
