#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Sat Oct 28 00:12:07 2017

#@author: param2020218


import sqlite3 as sq


#CONNECT FUCNTION-------------------------------------------------------------
def connect():
    conn = sq.connect("studentprof.db")
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS studentprof
        (id INTEGER PRIMARY KEY, grade INTEGER, section TEXT,
         name TEXT, phone_number INTEGER, gender TEXT, category TEXT,
         basketball TEXT, vocational TEXT, field TEXT, quiz TEXT,
         other_events TEXT, table_tennis TEXT, drama TEXT, track TEXT,
         cricket TEXT, swimming TEXT, football TEXT, music TEXT,
         email TEXT)"""
         )
    conn.commit()
    conn.close()

#ADD ENTRY FUCNTION------------------------------------------------------------
def insert(grade, section, name, phone_number, gender, category, basketball,
    vocational, field, quiz, other_events, table_tennis, drama, track,
    cricket, swimming, football, music, email):
    conn=sq.connect("studentprof.db")
    cur=conn.cursor()
    cur.execute(
                """INSERT INTO studentprof VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (grade, section, name, phone_number, gender, category, basketball,
         vocational, field, quiz, other_events, table_tennis, drama, track,
         cricket, swimming, football,music, email)
         )
    conn.commit()
    conn.close()

#VIEW ALL FUCNTION-------------------------------------------------------------
def view():
    conn = sq.connect("studentprof.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM studentprof")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#SEARCH FUNCTION---------------------------------------------------------------
def search(grade = "", section ="", name="", phone_number="", gender="",
           category= "", basketball = "", vocational ="", field = "", quiz = "",
           other_events = "", table_tennis = "", drama ="", track = "", cricket = "",
           swimming = "", football = "", music = "", email = ""):
    conn = sq.connect("studentprof.db")
    cur = conn.cursor()
    cur.execute(
            """SELECT * FROM studentprof WHERE grade=? OR section=? OR
            name=? OR phone_number=? OR gender=? OR category=? OR basketball=?
            OR vocational=? OR field=? OR quiz=? OR other_events=? OR
            table_tennis=? OR drama=? OR track=? OR cricket=? OR swimming=? OR
            football=? OR music=? OR email=?""", (grade, section, name,
            phone_number, gender, category, basketball, vocational, field,
            quiz, other_events, table_tennis, drama, track, cricket, swimming,
            football, music, email))
    rows = cur.fetchall()
    conn.close()
    return rows

#DELETE FUNCTION---------------------------------------------------------------
def delete(id):
    conn = sq.connect("studentprof.db")
    cur = conn.cursor()
    cur.execute("""DELETE FROM studentprof WHERE id = ?""",(id,))
    conn.commit()
    conn.close()

#UPDATE FUNCTION---------------------------------------------------------------
def update(id, grade, section, name, phone_number, gender, category, basketball,
         vocational, field, quiz, other_events, table_tennis, drama, track,
         cricket, swimming, football,music, email):
    conn = sq.connect("studentprof.db")
    cur = conn.cursor()
    cur.execute(
        """UPDATE studentprof SET grade=?, section=?,
        name=?, phone_number=?, gender=?, category=?, basketball=?,
        vocational=?, field=?, quiz=?, other_events=?, table_tennis=?,
        drama=?, track=?, cricket=?, swimming=?, football=?,
        music=?, email=? WHERE id = ?""",(grade, section, name, phone_number, gender,
        category, basketball, vocational, field, quiz, other_events,
        table_tennis, drama, track, cricket, swimming, football,
        music, email, id))
    conn.commit()
    conn.close()

connect()
