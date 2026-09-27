from fastapi_offline import FastAPIOffline


app= FastAPIOffline()


mylist= [10,20,30,40]
@app.get("/")
def home ():
    return {'hello' : 'world'}


@app.get("/home/")
def welcome():
    return{'welcom' : 'home'}


@app.get('/getall/')
def get_all_itme():
    return{'mylist' : mylist}


#===========================================================================
@app.post('/add/{new_item}')
def add_item(new_item:int):
    mylist.append(new_item )
    return{'mylist' : mylist}

#بالالیی و پایینی یکی هستن ولی دوتا روش هستن

@app.post('/addItem')
def add_item_by_insert(index:int , newitem: int):
    if index < len(mylist):
        mylist.insert(index  , newitem )
        return {f'{newitem} added in {index} posision'}
    else:
        return{f'{index} posision is out of range'}

#url = http://127.0.0.1:8000/add/11 ---> request.post(url)
#url = http://127.0.0.1:8000/addItem?index=2&newitem=123 -->>request.post(url, params)



#===========================================================================
@app.delete('/deleter/{item}')
def delete_by_mylist(item:int):
    if item in mylist:
        mylist.remove(item)
        return {f'{item} removed from mylist'}
    else:
        return {f"{item} not found"}


@app.delete('/deleteindex/')
def delete_by_index(index:int):
    if index < len(mylist):
        mylist.pop(index )

        return {f'deleted from {index} posision , mylist is {mylist}'}
    else:
        return{f'{index} posision not found'}



#===========================================================================
@app.put('/update/')
def update(old_item:int , new_item:int):

    if old_item in mylist:
        index = mylist.index(old_item)
        mylist[index] = new_item
        return {f'new mylist after update: {mylist}'}
    else:
        return{f'{old_item} Not found'}


@app.put('/updateindex/')
def update_by_index(index:int, new_item:int):
    if index < len (mylist):
        mylist[index] =  new_item
        return {f'new mylist after update: {mylist}'}
    else:
        return{f'{index} posision not found'}
