import flet as ft
import asyncio
from datetime import timedelta


class Stopwatch:
    def __init__(self):
        self.running = False
        self.elapsed_time = 0  # in seconds

    def reset(self):
        self.elapsed_time = 0
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def tick(self):
        if self.running:
            self.elapsed_time += 1


def main(page: ft.Page):
    page.title = "Stopwatch"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # ✅ Small screen and always on top
    page.window.width = 250
    page.window.height = 300
    page.window.resizable = False
    page.window.always_on_top = True
    # page.update()

    stopwatch = Stopwatch()
    time_display = ft.Text(value="00:00:00", size=40, weight="bold")

    async def update_time():
        while True:
            await asyncio.sleep(1)
            stopwatch.tick()
            td = str(timedelta(seconds=stopwatch.elapsed_time))
            time_display.value = td.split('.')[0]
            page.update()

    def start_clicked(e):
        stopwatch.start()

    def stop_clicked(e):
        stopwatch.stop()

    def reset_clicked(e):
        stopwatch.reset()
        time_display.value = "00:00:00"
        page.update()

    start_button = ft.ElevatedButton("Start", on_click=start_clicked)
    stop_button = ft.ElevatedButton("Stop", on_click=stop_clicked)
    reset_button = ft.ElevatedButton("Reset", on_click=reset_clicked)

    page.add(
        ft.Column(
            [
                time_display,
                ft.Row([start_button, stop_button, reset_button], alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.run_task(update_time)

ft.app(target=main)
