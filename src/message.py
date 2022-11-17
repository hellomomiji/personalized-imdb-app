from flask import Flask, render_template

def success(message):
    return render_template('message.html', mainMessage="Success! ", detailMessage=message)

def render_error(message):
    return render_template('message.html', mainMessage="Something went wrong.", detailMessage=message)