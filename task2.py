#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


G = nx.Graph()

G.add_nodes_from([1,2,3,4])

G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])

nx.draw(G, with_labels=True)


# In[4]:


nx.has_path(G, 3, 4)


# In[5]:


list(nx.all_simple_paths(G, 3, 4))


# In[6]:


nx.shortest_path(G, 3, 4)


# In[7]:


nx.shortest_path_length(G, 3, 4)


# In[8]:


nx.is_connected(G)


# In[9]:


nx.is_connected(G)


# In[18]:


G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])
nx.add_cycle(G,(1,2,3,4,5))
G.add_edge(6,7)

nx.draw(G, with_labels=True)


# In[19]:


nx.is_connected(G)


# In[20]:


nx.has_path(G, 3, 5)


# In[21]:


nx.shortest_path(G, 3, 5)


# In[22]:


nx.number_connected_components(G)


# In[23]:


list(nx.connected_components(G))


# In[24]:


components = list(nx.connected_components(G))
len(components[0])


# In[25]:


max(nx.connected_components(G), key=len)


# In[26]:


core_nodes = max(nx.connected_components(G), key=len)
core = G.subgraph(core_nodes)

nx.draw(core, with_labels=True)


# In[27]:


D = nx.DiGraph()
D.add_edges_from([
    (1,2),
    (2,3),
    (3,2), (3,4), (3,5),
    (4,2), (4,5), (4,6),
    (5,6),
    (6,4),
])
nx.draw(D, with_labels=True)


# In[28]:


nx.has_path(D, 1, 4)


# In[29]:


nx.has_path(D, 4, 1)


# In[30]:


nx.shortest_path(D, 2, 5)
nx.shortest_path(D, 5, 2)


# In[31]:


nx.is_strongly_connected(D)


# In[32]:


nx.is_weakly_connected(D)


# In[34]:


list(nx.weakly_connected_components(D))


# In[35]:


list(nx.strongly_connected_components(D))


# In[ ]:





# In[ ]:




