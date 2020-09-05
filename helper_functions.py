# from main import Patient


def combine_results(patients):
    output = []
    for patient in patients:
        patient_data = allocate_data(patient)
        output.append(patient_data)
    return output


def allocate_data(patient):
    patient_data = {'first_name': patient.first_name,
                    'last_name': patient.last_name,
                    'address': patient.address,
                    'date_of_birth': patient.date_of_birth,
                    'postal_code': patient.postal_code,
                    'breathing_difficulty': patient.breathing_difficulty,
                    'conscious': patient.conscious,
                    'pain': patient.pain,
                    'bleeding': patient.bleeding,
                    'additional_info': patient.additional_info,
                    }
    return patient_data
