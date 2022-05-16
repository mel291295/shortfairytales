import streamlit as st

st.title("Once upon a time")
st.subheader("This is a web app to summarize and translate Grimm's fairy tales")
st.caption("You can choose your favorite fairy tale and the app will summerize it for you into a few lines in whatevere language you want.")

uploaded_file = st.file_uploader("Choose a file", )
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)

option = st.selectbox("Which fairytale you want to summarize?", 
                      ("Little Snow White", "The Ugly Duckling", "Aladdin and the Wonderful Lamp", "The Sleeping Beauty", "Puss-in-Boots", "Adventures of Tom Thumb", "The Three Bears", "The Little Match Girl", "Beauty and the Beast", "The Story of Cinderella", "Jack the Giant Killer", "Jack and the Beanstalk", "Dick Whittington and His Cat", "The Story of Bluebeard", "Little Red Riding-Hood", "Sindbad the Sailor", "Hansel and Gretel", "The Goose Girl"))
st.write("You selected: ", option)

