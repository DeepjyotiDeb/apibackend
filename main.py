from sqlalchemy import desc
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import schemas, models
from .database import get_db, engine
from fastapi.middleware.cors import CORSMiddleware
from .routers import authentication
from fastapi import APIRouter
from .hashing import Hash
from mangum import Mangum

router = APIRouter
app = FastAPI(
    # root_path="/dev3/"
    )
models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
from .oauth21 import get_current_user

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://main.dlbzvtimfz2pv.amplifyapp.com/", "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', tags = ['blogs']) # all posts
def sanity(db:Session = Depends(get_db)):
    posts = db.query(models.BlogDetails).all()
    return (posts, "hello boi")

@app.get('/posts', tags = ['blogs']) # all posts
def show_posts(db:Session = Depends(get_db)):
    posts = db.query(models.BlogDetails).order_by(models.BlogDetails.created_on.desc()).all()
    return {
        "posts": posts,
        # "origins":origins
    }

@app.post('/create-posts/{uid}', tags = ['blogs'])
def create_post(uid: int, user: schemas.Blogger, 
                db:Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)
                ):
# @app.post('/create-posts', tags = ['blogs'])
# def create_post(user: schemas.Blogger, 
#                 db:Session = Depends(get_db)
#                 ):
    post = models.BlogDetails(
                              title = user.title, 
                              summary = str(user.summary), 
                              body = str(user.body),
                               user_id = uid)#user id from from front end
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.get("/get-post/{post_id}",  tags = ['blogs'])
def read_item( post_id: int, db:Session = Depends(get_db)):
    post = db.query(models.BlogDetails).get(post_id)
    # user = db.query(models.User).get
    return {"post_id": post_id, "post": post, }
    # return post

@app.put('/update-post/{post_id}', tags = ['blogs'])
def update_post(post_id: int, item: schemas.Update_Post, db:Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    print("IM HERE")
    update_post = db.query(models.BlogDetails).filter(models.BlogDetails.id == post_id).one_or_none()
    for var, value in vars(item).items():
        setattr(update_post, var, value) if value else None

    db.add(update_post)
    db.commit()
    db.refresh(update_post)
    return (update_post)

@app.delete('/delete-post/{id}', tags = ['blogs'])
def delete_post(id: int, db:Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db.query(models.BlogDetails).filter(models.BlogDetails.id == id).delete(synchronize_session=False)
    db.commit()
    return "post deleted"


@app.post('/user', response_model=schemas.ShowUser, tags = ['user'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # hashed_password = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt())
    new_user = models.User(name = request.name,
                           email = request.email,
                        #    password = request.password,)
                           password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request

@app.get('/show-user/', tags = ['user'])
def show_users(db:Session = Depends(get_db)):
    user = db.query(models.User).all()
    return user

@app.get('/get-user/{uid}', response_model=schemas.ShowUser, tags = ['user'])
def show_user(uid: int, db:Session = Depends(get_db)):
    user = db.query(models.User).order_by(models.BlogDetails.created_on.desc()).get(uid)
    return user

@app.delete('/delete-user/{id}', tags = ['user'])
def delete_user(id: int, db:Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    return "user deleted"

# handler = Mangum(app)
