from shiny import ui

def subgroups_filter_ui(id):
    gender_choice=["Female", "Male"]
    imagine_choice=["Done", "Not done"]
    prenotification_choices=["Prenotified", "Not prenotified"]
    mrs_choice = ["1", "2", "3", "4", "5", "6"]
    return ui.card(
        ui.card_header(
            ui.h5("Sub Groups"),
        ),
        ui.input_checkbox_group(id=f"list_gender_{id}", label="Genders shown in plot", choices=gender_choice, selected=gender_choice),
        ui.input_checkbox_group(id=f"list_imagine_{id}", label="Imaging of patients shown in plot", choices=imagine_choice, selected=imagine_choice),
        ui.input_checkbox_group(id=f"list_prenotifiction_{id}", label="Prenotification of patients in plot", choices=prenotification_choices, selected=prenotification_choices),
        ui.input_checkbox_group(id=f"list_mrs_{id}", label="mRS of patients in plot", choices=mrs_choice, selected=mrs_choice),
    ),
