"""
Дан дата фрейм состоящий из 2 колонок: start_datetime, end_datetime.
В каждой строке написано время начала и окончания проверки технической готовности
самолета к вылету для которой требуется один инженер.
Преобразуйте этот датафрейм в датафрейм, в котором для каждой минуты будет написано,
сколько в эту минуту в аэропорту будет работать инженеров и найдите максимальное значение
потребности в инженерах. В ответе укажите только одно число.
"""

import task_pandas as pd

def max_eng_per_minute(df: pd.DataFrame) -> int:
    df = df.copy()
    df["start_datetime"] = pd.to_datetime(df["start_datetime"]).dt.floor("min")
    df["end_datetime"] = pd.to_datetime(df["end_datetime"]).dt.floor("min")

    minutes = []

    for _, row in df.iterrows():
        rng = pd.date_range(
            start=row["start_datetime"],
            end=row["end_datetime"] - pd.Timedelta(minutes=1),
            freq="min"
        )
        minutes.append(pd.DataFrame({"minute": rng, "engineers": 1}))

    timeline = (
        pd.concat(minutes, ignore_index=True)
        .groupby("minute", as_index=False)["engineers"]
        .sum()
    )

    return int(timeline["engineers"].max())
