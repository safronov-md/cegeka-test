from app import app
from flask import jsonify, make_response
from .cv import PERSONAL_BLOCK, EXPERIENCE_BLOCK, EDUCATION_BLOCK
from .tools import DictionaryPrinter


@app.route('/', methods=['GET',])
def main_page():
    return "\n".join(["- GET /personal;","- GET /experience;","- GET /education"])

@app.cli.command("get-personal-info")
@app.route('/personal',methods=['GET',])
def personal_block():
    """
        Endpoint gets dict with personal data from cv module.

        Good practice will to check if PERSONAL_BLOCK isn't empty, before
        sending response. And in case, when it's empty we can send 404 with
        detail message. But in this case, we have hard coded data and we don't
        need to check it. <--- This also applies to other endpoints of this task
    """
    print(f'Personal block:')
    dprinter = DictionaryPrinter(PERSONAL_BLOCK)
    dprinter.print_data()
    return make_response(jsonify(PERSONAL_BLOCK),200)

@app.cli.command("get-experience-info")
@app.route('/experience',methods=['GET',])
def experience_block():
    """
        Endpoint gets dict with experience data from cv module
    """
    print(f'Experience block: \n')
    for experience in EXPERIENCE_BLOCK:
        dprinter = DictionaryPrinter(experience)
        dprinter.print_data()

    return make_response(jsonify(EXPERIENCE_BLOCK),200)

@app.cli.command("get-education-info")
@app.route('/education',methods=['GET',])
def education_block():
    """
        Endpoint gets dict with education data from cv module
    """
    print(f'Educational block: \n')
    for education in EDUCATION_BLOCK:
        dprinter = DictionaryPrinter(education)
        dprinter.print_data()
    return make_response(jsonify(EDUCATION_BLOCK),200)
