# test: PR-scan verification for the new Gemma 4 26B-A4B-NVFP4 governance model
DB_PASSWORD = "TestSecret123!"

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return db.execute(query)
