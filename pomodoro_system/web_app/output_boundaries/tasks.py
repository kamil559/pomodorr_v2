from flask import make_response, jsonify

from pomodoros import (
    PausePomodoroOutputBoundary,
    PausePomodoroOutputDto,
    ReactivateTaskOutputBoundary,
    ReactivateTaskOutputDto,
    PinTaskToProjectOutputBoundary,
    PinTaskToProjectOutputDto,
)
from serializers.tasks import CompleteTaskSchema, ReactivateTaskSchema, PinTaskToProjectSchema


class JSONCompleteTaskOutputBoundary(PausePomodoroOutputBoundary):
    def present(self, output_dto: PausePomodoroOutputDto) -> None:
        serialized_output_data = CompleteTaskSchema().dump(output_dto)
        self.response = make_response(jsonify(serialized_output_data), 200)


class JSONReactivateTaskPresenter(ReactivateTaskOutputBoundary):
    def present(self, output_dto: ReactivateTaskOutputDto) -> None:
        serialized_output_data = ReactivateTaskSchema().dump(output_dto)
        self.response = make_response(jsonify(serialized_output_data), 200)


class JSONPinTaskToProjectPresenter(PinTaskToProjectOutputBoundary):
    def present(self, output_dto: PinTaskToProjectOutputDto) -> None:
        serialized_output_data = PinTaskToProjectSchema().dump(output_dto)
        self.response = make_response(jsonify(serialized_output_data), 200)
