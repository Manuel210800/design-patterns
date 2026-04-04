from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


class MovieConfigVisitor(ABC):
    @abstractmethod
    def visit_management_settings(self, settings: ManagementSettings) -> None:
        pass

    @abstractmethod
    def visit_communication_settings(self, settings: CommunicationSettings) -> None:
        pass

    @abstractmethod
    def visit_booking_questions(self, questions: BookingQuestions) -> None:
        pass


class MovieConfig(ABC):
    @abstractmethod
    def accept(self, visitor: MovieConfigVisitor) -> None: ...


@dataclass
class ManagementSettings(MovieConfig):
    partnership_type: str
    purchase_terms: str | None

    def accept(self, visitor: MovieConfigVisitor) -> None:
        visitor.visit_management_settings(self)

@dataclass
class CommunicationSettings(MovieConfig):
    email_template: str
    pdf_template: str

    def accept(self, visitor: MovieConfigVisitor) -> None:
        visitor.visit_communication_settings(self)

@dataclass
class BookingQuestions(MovieConfig):
    question_ids: list[str]
    optional: bool

    def accept(self, visitor: MovieConfigVisitor) -> None:
        visitor.visit_booking_questions(self)

class PropagateToMainPlansVisitor(MovieConfigVisitor):
    def __init__(self, main_plan_ids: list[int]) -> None:
        self._main_plan_ids = main_plan_ids

    def visit_management_settings(self, settings: ManagementSettings) -> None:
        for plan_id in self._main_plan_ids:
            print(
                f"  [Propagate] MainPlan {plan_id} ← "
                f"partnership_type={settings.partnership_type}"
            )

    def visit_communication_settings(self, settings: CommunicationSettings) -> None:
        for plan_id in self._main_plan_ids:
            print(
                f"  [Propagate] MainPlan {plan_id} ← "
                f"email_template={settings.email_template}"
            )

    def visit_booking_questions(self, questions: BookingQuestions) -> None:
        for plan_id in self._main_plan_ids:
            print(
                f"  [Propagate] MainPlan {plan_id} ← "
                f"questions={questions.question_ids}, optional={questions.optional}"
            )


class ValidateConfigVisitor(MovieConfigVisitor):
    def visit_management_settings(self, settings: ManagementSettings) -> None:
        if settings.partnership_type not in ("marketplace_api", "affiliate"):
            print(f"  [Validate] INVALID partnership_type: {settings.partnership_type}")
        else:
            print(f"  [Validate] ManagementSettings OK")

    def visit_communication_settings(self, settings: CommunicationSettings) -> None:
        if not settings.email_template:
            print(f"  [Validate] MISSING email_template")
        else:
            print(f"  [Validate] CommunicationSettings OK")

    def visit_booking_questions(self, questions: BookingQuestions) -> None:
        if len(questions.question_ids) == 0:
            print(f"  [Validate] EMPTY question list")
        else:
            print(f"  [Validate] BookingQuestions OK ({len(questions.question_ids)} questions)")

def propagate_movie_configuration(
    configs: list[MovieConfig],
    visitors: list[MovieConfigVisitor],
) -> None:
    for visitor in visitors:
        print(f"\n--- Running {visitor.__class__.__name__} ---")
        for config in configs:
            config.accept(visitor)


if __name__ == "__main__":
    movie_configs: list[MovieConfig] = [
        ManagementSettings(partnership_type="marketplace_api", purchase_terms="No refunds"),
        CommunicationSettings(email_template="cinema_confirmation_v2", pdf_template="ticket_v1"),
        BookingQuestions(question_ids=["q-seat-pref", "q-accessibility"], optional=False),
    ]

    visitors: list[MovieConfigVisitor] = [
        PropagateToMainPlansVisitor(main_plan_ids=[101, 102, 103]),
        ValidateConfigVisitor(),
    ]

    propagate_movie_configuration(movie_configs, visitors)
