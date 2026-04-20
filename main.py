from flask import Flask, jsonify
from prisma import Prisma

app = Flask(__name__)

@app.route("/student", methods=["GET"])
async def list_Students():
    prisma = Prisma()
    await prisma.connect()

    # read data
    ### find_first, find_many, find_unique

    # write
    ## create, create_many

    # update
    ## update, update_many

    # delete
    ## delete, delete_many
    student = await prisma.student.find_first()

    student_dict = student.model_dump()

    return jsonify(student_dict), 200

if __name__ == "__main__":
    app.run(debug=True)