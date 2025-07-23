import collections.abc
import typing

from aviation._model import Transform


class SystemsModel:
    """A system of models formed by a sequence of transforms."""

    def __init__(self, transforms: collections.abc.Sequence[Transform[typing.Any, ...]]) -> None:
        """Initialise the system model from a sequence of transforms."""
        self.transforms = set(transforms)

    def evaluate(self, inputs: dict[str, typing.Any], output: str) -> typing.Any:  # noqa: ANN401
        """Calculate the value returned by a transform."""
        # If the requested `output` has already been supplied as an input then this can be returned
        # directly without need for computation.
        if output in inputs:
            return inputs[output]

        # The request `output` is not in `inputs` so it must be the name of a transform in
        # `self.transforms`. If it's not found in `self.transforms` then there must be an error.
        for transform in self.transforms:
            if transform.name == output:
                break
        else:
            message = f"No transform with name {output}"
            raise ValueError(message)

        # To evaluate the `transform`, arguments for all of its parameters are required. If a
        # parameter is not found in the inputs, evaluate that parameter from its own transform.
        for parameter in transform.parameters:
            if parameter not in inputs:
                inputs[parameter] = self.evaluate(inputs, parameter)

        # Evaluate and return the `transform` associated with the passed `output`.
        arguments = {parameter: inputs[parameter] for parameter in transform.parameters}
        return transform(**arguments)
