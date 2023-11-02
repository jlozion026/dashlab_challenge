import os
from dashlabs import ColumnCleaning


def generate_csv_files(entry_1):
    source_json_folder = 'output_json'
    target_csv_folder = "output_csv_folder"

    if os.path.exists(source_json_folder) and os.path.isdir(source_json_folder):
        folder_list = [folder for folder in os.listdir(source_json_folder) if os.path.isdir(os.path.join(source_json_folder, folder))]
        for folder in folder_list:
            try:
                # HIV Certificate
                if folder == "hiv_cert_json":
                    personal_data = [
                    'form name', 'certify name', 'physician', 'license number', 'date medical exam',
                    'date', 'name', 'age', 'gender', 'civil status', 'address'
                    ]
                    results_and_other_details = [
                    'screening test', 'result','technologist', 'hiv cert number', 'expiry date', 'pathologist'
                    ]
            
                    column_order = [*personal_data, *results_and_other_details]

                # Medical Landbase Certificate
                elif folder == "med_landbase_cert_json":
                    personal_data = [
                        "form name","last name","first name","middle name","age","date of birth","place of birth",
                        "nationality","gender", "civil status","religion","address","passport number",
                        "destination","position", "employer"
                    ]
                    evaluation = [
                        "satisfactory hearing", "satisfactory sight", "satisfactory colour vision", "satisfactory psych test",
                        "suffer med condition", "result", "physician", "exam date", "medical director", "date sign", 
                        "issued date", "expiration date"
                    ]    
                    column_order = [*personal_data, *evaluation]        
            
                # Medical Seafarers Certificate
                elif folder == "med_seafarers_cert_json":
                    personal_data = [
                    'form name', 'surname', 'first name', 'middle name', 'age', 'date of birth', 'place of birth',
                    'nationality', 'gender', 'civil status', 'religion', 'address', 'passport number', 'seaman book number',
                    'position', 'company']
                    declarations = [
                    'documents checked', 'hearing stwcode', 'unaided hearing', 'visual acuity', 'colour vision', 
                    'date of last colour vision test', 'visual', 'lookout duties', 'restrictions', 'suffer med condition'
                    ]
                    other_details = [
                    'exam given to', 'result', 'physician', 'date of exam', 'med director', 'issuing auth', 'address auth',
                    'certifying auth', 'license number', 'seaferer signature', 'signature date', 'date of issuance', 'date of expiry'
                    ]
                
                    column_order = [*personal_data, *declarations, *other_details]
            
                # Medical Landbase Exam
                elif folder == "med_landbase_exam_json":
                    personal_data = [
                    "form name","last name","first name","middle name","age","date of birth","place of birth",
                    "nationality","gender", "civil status","religion","address","passport number",
                    "destination","position", "company"
                    ]
                    medical_history = [
                    "head injury", "frequent headache", "frequent dizziness", "neurological disorder",
                    "sleep disorder", "mental disorder", "eye problem","ear disorder", "nose or throat disorder",
                    "tuberculosis", "lung disorder", "high blood pressure", "heart disease", "rheumatic",
                    "diabetes","endocrine disorder", "cancer or tumor", "blood disorder", "stomach pain",
                    "abdominal disorder", "gynaecological disorder", "bladder disorder", "back or joint injury",
                    "familial disorder", "sexually transmitted disease", "tropical disease", "schistosomiasis",
                    "asthma", "allergies", "operation/s", "signed of as sick", "hospitalized", "declared unfit for work overseas",
                    "medical cert been restricted", "aware to any medical problem", "feel fit", "allergic medication", 
                    "taking medication"
                    ]
                    medical_exam = [
                    "height","weight","blood pressure","pulse rate","rhythm","respiration","bmi",
                    "far vision uncorrected", "far vision corrected", "near vision uncorrected",
                    "near vision corrected", "ishihara color vision", "hearing right ear", "hearing left ear",
                    "clarity speech", "skin", "head neck scalp", "eyes external", "pupils", "ears", 
                    "nose sinus", "mouth throat", "neck", "chest", "lungs", "heart", "abdomen", "back",
                    "anus rectum",  "genito urinary system", "inguinals genitals", "extremities", "reflexes",
                    "dental"
                    ]
                    results = [
                    "xray", "ecg", "cbc", "urinalysis", "stool", "hepa", "hiv test", "rpr", "blood type",
                    "psychological test", "additional test"
                    ]
                    summary = [
                    "basic doh med exam", "additional test", "host med lab", "result"
                    ]
                    other_details = [
                    "date med exam", "date med expire", "med exam report number", "physician", "license number",
                    "clinic address", "clinic name", "date sign"
                    ]
            
                    column_order = [*personal_data, *medical_history, *medical_exam, *results, *summary, *other_details]
                
                # Medical Seafarers Exam
                elif folder == "med_seafarers_exam_json":
                    personal_data = [
                        "form name","last name","first name","middle name","age","date of birth","place of birth",
                        "nationality","gender", "civil status","religion","address","passport number",
                        "seaman book number","position", "employer"
                    ]
                    medical_history = [
                        "head injury", "frequent headache", "frequent dizziness", "neurological disorder",
                        "sleep disorder", "mental disorder", "eye problem","ear disorder", "nose or throat disorder",
                        "tuberculosis", "lung disorder", "high blood pressure", "heart disease", "rheumatic",
                        "diabetes","endocrine disorder", "cancer or tumor", "blood disorder", "stomach pain",
                        "abdominal disorder", "gynaecological disorder", "last menstrual period" , "bladder disorder", "back or joint injury",
                        "familial disorder", "sexually transmitted disease", "tropical disease", "schistosomiasis",
                        "asthma", "allergies", "operation/s", "signed of as sick", "hospitalized", "declared unfit for sea duty",
                        "medical cert been restricted", "aware to any medical problem", "feel fit", "allergic medication", 
                        "taking medication"
                    ]
                    medical_exam = [
                        "height","weight","blood pressure","pulse rate","rhythm","respiration","bmi",
                        "far vision uncorrected", "far vision corrected", "near vision uncorrected",
                        "near vision corrected", "ishihara color vision", "hearing right ear", "hearing left ear",
                        "clarity speech", "skin", "head neck scalp", "eyes external", "pupils", "ears", 
                        "nose sinus", "mouth throat", "neck", "chest", "lungs", "heart", "abdomen", "back",
                        "anus rectum",  "genito urinary system", "inguinals genitals", "extremities", "reflexes",
                        "dental",
                    ]
                    results = [
                        "xray", "ecg", "cbc", "urinalysis", "stool", "hepa", "hiv test", "rpr", "blood type",
                        "psychological test", "additional lab test"
                    ]
                    summary = [
                        "basic doh med exam", "additional lab", "host med lab", "remarks"
                    ]
                    assessment = [
                        "result", "deck service", "engine service", "catering service", "other services", "restrictions", "visual aids"
                    ]
                    other_details = [
                        "date med exam", "date med expire", "med exam report number", "physician", "license number",
                        "clinic address", "applicant signature", "date sign"
                    ]

                    column_order = [*personal_data, *medical_history, *medical_exam, *results, *summary, *assessment,*other_details]

                # Psychological Evaluation Form
                elif folder == "psycho_eval_json":
                    personal_data = [
                        "form name","name", "position applied for", "referred by", "date of examination"
                    ]
                    test_administered = [
                        "intelligence test", "personality test", "other tests", "intellectual level"
                    ]
                    sense_of_responsibility = [
                        "perseverance","obedience","self discipline", "enthusiasm", "initiative"
                    ]
                    emotional_stability = [
                        "can withstand boredom and work alone", "tolerance to stress pressures and inconveniences", "faces reality"
                    ]
                    objectivity = [
                        "tough mindedness", "adaptability", "practicality"
                    ]
                    motivation = [
                        "assertiveness", "independence", "resourcefulness"
                    ]
                    interpersonal_and_personal_adjustment = [
                        "teammanship", "deference", "self esteem", "aggressive tendencies"
                    ]
                    goal_orientation = [
                        "directs ones effort towards clear cut objectives",
                    ]
                    other_details = [
                        "remarks", "psychologist"
                    ]

                    column_order = [*personal_data, *test_administered, *sense_of_responsibility, *emotional_stability, *objectivity, *motivation,*interpersonal_and_personal_adjustment, *goal_orientation, *other_details]        
        
                else:
                    print(f"Skipping folder: {folder}")
            except OSError as e:
                # Handle the error when the folder is empty or encounters any other issues
                print(f"Error processing folder {folder}: {str(e)}")                

            combiner = ColumnCleaning(folder, target_csv_folder, entry_1) 
            combiner.combine_json_to_csv(column_order)
            