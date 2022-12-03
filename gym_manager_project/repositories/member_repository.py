from db.run_sql import run_sql

from models.member import Member




def save(member):
    sql = """ INSERT into members 
    (name, email, status, type) 
    VALUES (%s, %s, %s, %s) 
    RETURNING * """
    values = [member.name, member.email, member.status, member.type]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = """ DELETE from members """
    run_sql(sql)

def delete(id):
    sql = """ DELETE from members where id = %s"""
    values = [id]
    run_sql(sql, values)

def select_all():
    members = []
    sql = """SELECT * FROM members"""
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['email'], row['status'], row['type'], row['id'])
        members.append(member)
    return members

def select(id):
    sql = """SELECT * from members WHERE id = %s"""
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['name'], result['email'], result['status'], result['type'], result['id'])
    return member

def update(member):
    sql = """UPDATE members 
    SET (name, email, status, type) = (%s, %s, %s, %s) 
    WHERE id = %s"""

    values = [member.name, member.email, member.status, member.type, member.id]
    run_sql(sql, values)
