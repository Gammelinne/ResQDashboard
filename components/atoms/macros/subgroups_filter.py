from shiny import ui

def subgroups_filter_ui(id):
    gender_choice = {
        "0": "Female", 
        "1": "Male"
    }
    imagine_choice= {
        "1": "Done",
        "0": "Not done"
    }
    prenotification_choices= {
        "1": "Prenotified", 
        "0": "Not prenotified"
    }
    mrs_choice = ["1", "2", "3", "4", "5", "6"]
    return ui.card(
        ui.card_header(
            ui.h5("Sub Groups"),
        ),
        ui.input_checkbox_group(id=f"list_gender_{id}", label="Genders shown in plot", choices=gender_choice, selected=list(gender_choice.keys())),
        ui.input_checkbox_group(id=f"list_imagine_{id}", label="Imaging of patients shown in plot", choices=imagine_choice, selected=list(imagine_choice.keys())),
        ui.input_checkbox_group(id=f"list_prenotifiction_{id}", label="Prenotification of patients in plot", choices=prenotification_choices, selected=list(prenotification_choices.keys())),
        ui.input_checkbox_group(id=f"list_mrs_{id}", label="mRS of patients in plot", choices=mrs_choice, selected=mrs_choice),
    ),
