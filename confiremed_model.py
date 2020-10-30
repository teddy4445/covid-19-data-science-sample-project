# library imports

# project imports


class ConfirmedModel:
    """

    """

    def __init__(self,
                 y_model: list,
                 y_data: list,
                 model_parameter,
                 model_function,
                 model_name: str,
                 label: str,
                 fitness: float):
        self.y_model = y_model
        self.y_data = y_data
        self.model_parameter = model_parameter
        self.model_function = model_function
        self.fitness = fitness
        self.model_name = model_name
        self.label = label
