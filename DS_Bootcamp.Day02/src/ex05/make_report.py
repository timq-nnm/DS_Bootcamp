import sys
from analytics import Research
from config import NUM_OF_STEPS, FILENAME, FILE_EXTENSION, TEMPLATE

if __name__ == '__main__':
    research = Research(sys.argv)
    data = research.file_reader()
    data_calc = research.Calculations(data)
    data_analyt = research.Analytics(data)

    total = len(research.file_reader())
    tails, heads = data_calc.count()
    tails_percent, heads_percent = data_calc.Fractions()
    forecast_total, forecast_tails, forecast_heads = data_analyt.predict_random_count(data_analyt.predict_random(NUM_OF_STEPS))


    result = TEMPLATE.format(
        total=total,
        tails=tails,
        heads=heads,
        tails_percent="{:.2f}".format(tails_percent),
        heads_percent="{:.2f}".format(heads_percent),
        forecast_total=forecast_total,
        forecast_tails=forecast_tails,
        forecast_heads=forecast_heads
    )

    Research.Analytics.save_file(result, FILENAME, FILE_EXTENSION)