import wolframalpha
query=str(input('Enter any query related to computation: '))
def computation(query):
    client=wolframalpha.Client('VTY239-55Y8AXJEW4')
    res=client.query(query)
    result=next(res.results).text
    print(result)
    return result

computation(query)


if __name__=="_main_":
    computation(query)


