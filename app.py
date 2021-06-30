from flask import Flask,render_template,url_for,request,redirect
import psycopg2

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URL']='SQLITE:///test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db=SQLAlchemy(app)
import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="todo_app",
    user="postgres",
    password="cheesecake222"
)
cur=conn.cursor()
# class Todo(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     content=db.Column(db.String(200),nullable=False)
#     date_created=db.Column(db.DateTime,default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return '<Task %r>'%self.id

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        task_content=request.form['content']

        try:
            cur.execute('INSERT INTO todo(content) VALUES (%s)',(task_content,))
            conn.commit()
            return redirect('/')
        except:
            return 'could not post'
    else:
        try:
            cur.execute('SELECT * FROM todo ORDER BY date_created')
            rows=cur.fetchall()
        except:
            return 'could not get'  
        return render_template("index.html",tasks=rows)

@app.route('/delete/<int:id>')
def deleteTask(id):
    cur.execute('DELETE FROM todo WHERE id=%s',(id,))
    conn.commit()
    return redirect('/')

@app.route('/update/<int:id>',methods=['GET','POST'])
def updateTask(id):
    cur.execute('SELECT * FROM todo WHERE id=%s',(id,))
    query=cur.fetchone()

    if request.method=='POST':
        task_content=request.form['content']
        cur.execute('UPDATE todo SET content=%s WHERE id=%s',(task_content,id))
        conn.commit()
        return redirect('/')
    else:
        return render_template('Update.html',task=query)

# cur.close()
# conn.close()

if __name__=="__main__":
    app.run(debug=True)