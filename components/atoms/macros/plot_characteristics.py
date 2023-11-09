from shiny import ui

def plot_characteristics_ui(id):
    return ui.card(
        ui.card_header(
            ui.h5("Plot characteristics")
        ),
        # Qi x-axis select input. 
        ui.output_ui(f"x_qi_selector_{id}"),
        ui.output_ui(f"x_selected_qi_value_{id}"),

        # Qi y-axis select input
        ui.output_ui(f"y_qi_selector_{id}"),
        ui.output_ui(f"y_selected_qi_value_{id}"),

        # Factor to compare select input
        ui.output_ui(f"factor_to_compare_{id}"),

        # Aggregation type
        ui.output_ui(f"aggregation_type_{id}"),
        
        # Mean checkbox 
        ui.output_ui(f"checkbox_mean_{id}"),

        # Median checkbox 
        ui.output_ui(f"checkbox_median_{id}"),

        # Trend checkbox
        ui.output_ui(f"checkbox_trend_{id}"),

        # error bars checkbox
        ui.output_ui(f"checkbox_error_bar_{id}"),

    ),
