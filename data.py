class node:
  def __init__(self, data):
    self.data = data
    self.next_node = None

class Message:
  def __init__(self ,user , id,data) :
    self.user = user
    self.id = id
    self.data = data


class chained_list:
  def __init__(self, data):
    self.first_node = node(data)
    self.last_node = self.first_node
    self.size = 1

  def __str__(self):
    txt = str(self.first_node.data)

    current_node = self.first_node
    while current_node.next_node != None:
      current_node = current_node.next_node
      txt += "-"+str(current_node.data)
    return txt

  def insert_first(self, data):
    N = self.first_node
    self.first_node = node(data)
    self.first_node.next_node = N
    self.size += 1

  def get_size(self):
    return self.size

  def append(self,data):
    new_last_node = node(data)
    self.last_node.next_node = new_last_node
    self.last_node = new_last_node
    self.size += 1


class hashtable_user: 
  def __init__(self, bucket_size):
    self.buckets = []
    for i in range(bucket_size):
      self.buckets.append([])

  def append2(self,key,value): # append(3,"coucou")
    hashed_key = hash(key)
    indice_bucket = hashed_key % len(self.buckets)
    self.buckets[indice_bucket].append((key,value))

  def get(self, key):
    hashed_key = hash(key)
    indice_bucket = hashed_key % len(self.buckets)
    for bucket_key,bucket_value in self.buckets[indice_bucket]:
      if bucket_key == key:
        return bucket_value
    return None
  

  
    
class list_chained_sorted:
    def __init__(self,data):
        self.first_node = node(data)
        self.last_node = self.first_node
    
    def add_data(self,data):
        current_node = self.first_node
        N = node(data)
        if data <self.first_node.data :
            N.next_node = self.first_node
            self.first_node = N
            return 
        if data > self.last_node.data :
            self.last_node.next_node = N
            self.last_node = N
            return
        while current_node.next_node.data <data :
            current_node = current_node.next_node

        N = node(data)
        N.next_node = current_node.next_node
        current_node.next_node = N

class Stack : #ajoute le dernier et supprime le dernier
  def __init__(self,data) : 
    self.last_node = node(data)
    self . next_last_node = self.last_node
    self.current_node = self.last_node
    self.items = []
    self.size =1
    
  def push(self,data) : #rajouter une donnée a la fin
    N = node(data)
    N.next_node = self.last_node
    self.last_node = N
    self.size +=1
  def tolist(self):
    current_node = self.last_node
    result = []
    while current_node is not None:
        result.append(str(current_node.data))
        current_node = current_node.next_node
        return result
  def pop(self) : #supprimé la derniere  et montrer la donnée 
    data = self.last_node.data
    self.last_node = self.last_node.next_node
    self.size -=1
    return data

  def size(self) : #montre la longeur de la donnée
    return self.size

  def peek(self) : # montrez le dernier
    return self.last_node.data
    
  def append1(self) : 
    global txt 
    txt = [] #
    current_node = self.last_node
    if current_node.data != None :
      while current_node.next_node != None :
        txt.append(str(current_node.data))
        current_node = current_node.next_node
    else :
      txt.append(str("error")) 
    return txt 

  def append3(self):
    current_node = self.last_node
    result = []
    while current_node is not None:
        result.append(current_node.data)
        current_node = current_node.next_node
    result.reverse() # inverse l'ordre pour avoir le plus ancien message en premier
    return result


  def goon(self) : 
    Stack.append1()
    for i in txt :
      return i 

  def goin(self):
        current_node = self.last_node
        result = []
        for i in range(2):
            if current_node is not None:
                result.append(str(current_node.data))
                current_node = current_node.next_node
        if len(result) == 2:
            self.last_node = current_node
            return '\n'.join(result)
        else:
            return None

  def forward(self):
    if self.current_node is not None and self.current_node.next_node is not None:
        self.current_node = self.current_node.next_node
        return self.current_node.data
    else:
        return None

  def backward(self):
    if self.current_node is not None and self.current_node != self.last_node:
        prev_node = self.last_node
        while prev_node.next_node != self.current_node:
            prev_node = prev_node.next_node
        self.current_node = prev_node
        return self.current_node.data
    else:
        return None


    

class Queue: #ajoute le dernier et on supprime le premier 
  def __init__(self,data):
    self.first_node = node(data)
  
  def __str__(self):
    return "coucou"

  def push(self,data):#rajouter une donnée a la fin
    if self.first_node == None : 
      self.first_node = node(data)
      return 
    
    current_node = self.first_node
    while current_node.next_node != None :
      current_node = current_node.next_node

    current_node.next_node= node(data)
    self.size +=1

  def pop(self): #supprime le premier
    data = self.first_node.data
    self.first_node = self.first_node.next_node
    self.size -=1
    return data

  def peek(self):# montrez le premier
    return self.first_node

  def size(self):
    return self.size

class queuecercle: #la derniere envoie a la repmiere donnée
  def __init__(self,data):
    self.first_node = node(data)
  
  def __str__(self):
    return "coucou"

  def push(self,data):#rajouter une donnée a la fin
    if self.first_node == None : 
      self.first_node = node(data)
      return 
    
    current_node = self.first_node
    while current_node.next_node != self.first_node :
      current_node = current_node.next_node

    current_node.next_node= node(data)
    self.size +=1

  def pop(self): #supprime le premier
    data = self.first_node.data

    current_node = self.first_node
    while current_node.next_node != None :
      current_node = current_node.next_node
    current_node.next_node = self.first_node
    self.first_node = self.first_node.next_node
    current_node.next_node.next_node= None
    self.size -=1
    return data

  def peek(self):# montrez le premier
    return self.first_node

  def size(self):
    return self.size
