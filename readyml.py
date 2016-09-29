import yaml as ym

# In[5]:

def yaml_load(file_path):
    ''' Read Data from a YAML file '''
    with open(file_path,'r') as file_descriptor:
        data = ym.load(file_descriptor)
    return data

#def yaml_dump(file_path):
#    ''' Dump Data to a YAML file '''
#    with open(file_path,'w') as file_descriptor:
#        yaml.dump(data, file_descriptor)




# In[25]:

if __name__ == "__main__":
    filepath = "SLA-descriptor/SLO/service-name-slo.yaml"
    data = yaml_load(filepath)


# In[19]:

    items = data


# In[39]:

    for item in data:
        print item.keys(), item.values()
        print "---"


# In[ ]:
