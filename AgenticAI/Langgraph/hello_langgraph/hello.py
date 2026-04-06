from typing import TypedDict
from urllib import response
from langgraph.graph import StateGraph,START,END

# Lets create state for our application
class MyState(TypedDict):
    '''This class represents the state of our graph
     It has a name, a list of friends, a list of family members and a message
        that we want to display on the graph
        We will use this state to create a graph that shows the relationships between the name, friends and family members
            and the message will be displayed on the graph as well
            
     '''
    name: str
    friends: list[str]
    family: list[str]
    message: str
    
# node 1
def find_friends(state: MyState) -> MyState:
    '''This function takes the state and returns the list of friends'''
    state['friends'] = ['Alice', 'Bob', 'Charlie']
    return state

# node 2
def find_family(state: MyState) -> MyState:
    '''This function takes the state and returns the list of family members'''
    state['family'] = ['Mom', 'Dad', 'Sister']
    return state

# Now we will create a graph that uses this state
graph = StateGraph(MyState)

# We will add the nodes to the graph
graph.add_node("friends", find_friends)
graph.add_node("family", find_family)

# We will add the edges to the graph
graph.add_edge(START, "friends")
graph.add_edge("friends", "family")
graph.add_edge("family", END)   

#Compile the graph
compiled_graph = graph.compile()    

if __name__ == "__main__":
   response = compiled_graph.invoke({"name": "John", "friends": [], "family": [], "message": "Hello, World!"})
   print(response)
    