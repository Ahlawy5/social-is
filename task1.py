#!/usr/bin/env python
# coding: utf-8

# In[6]:


import networkx as nx


# In[7]:


nx.__version__


# In[5]:



G = nx.Graph()


G.add_node('a')

nodes_to_add = ['b', 'c', 'd']
G.add_nodes_from(nodes_to_add)

G.add_edge('a', 'b')

edges_to_add = [('a', 'c'), ('b', 'c'), ('c', 'd')]
G.add_edges_from(edges_to_add)

nx.draw(G, with_labels=True)


# In[8]:


nx.draw(G,
        with_labels=True,
        node_color='blue',
        node_size=1600,
        font_color='white',
        font_size=16,
        )


# In[9]:


G.nodes()


# In[10]:


G.edges()


# In[11]:


for node in G.nodes:
    print(node)


# In[12]:


for edge in G.edges:
    print(edge)


# In[13]:


G.number_of_nodes()


# In[14]:


G.number_of_edges()


# In[15]:


G.neighbors('b')


# In[16]:


for neighbor in G.neighbors('b'):
    print(neighbor)


# In[17]:


list(G.neighbors('b'))


# In[18]:


nx.is_connected(G)


# In[19]:


G.has_node('a')


# In[20]:


G.has_node('x')


# In[21]:


'd' in G.nodes


# In[22]:


G.has_edge('a', 'b')


# In[23]:


G.has_edge('a', 'd')


# In[24]:


('c', 'd') in G.edges


# In[25]:


len(list(G.neighbors('a')))


# In[26]:


G.degree('a')


# In[31]:


items = ['spider', 'y', 'banana']
[item.upper() for item in items]


# In[33]:


print(G.nodes())
print([G.degree(n) for n in G.nodes()])

g = (len(item) for item in items)
list(g)
max(len(item) for item in items)
sorted(item.upper() for item in items)


# In[34]:


G = nx.Graph()

G.add_nodes_from(['cat','dog','virus',13])

G.add_edge('cat','dog')

nx.draw(G, with_labels=True, font_color='white', node_size=1000)


# In[41]:



D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])

nx.draw(D, with_labels=True)


# In[42]:


D.has_edge(1,2)
D.has_edge(2,1)

print('Successors of 2:', list(D.successors(2)))

print('Predecessors of 2:', list(D.predecessors(2)))


# In[43]:


D.in_degree(2)
D.out_degree(2)


# In[44]:


D.degree(2)
print('Successors of 2:', list(D.successors(2)))
print('"Neighbors" of 2:', list(D.neighbors(2)))


# In[ ]:




