import streamlit as st
from datetime import datetime
import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.figure_factory as ff
#
# OUTPUT TAGS
# # title
# st.title('Title - Hello Meenal')
#
# # header
# st.header('Header - Meenal')
#
# # subheader
# st.subheader('Header - Meenal')
#
# # text
# st.text('Text - Meenal')
#
# # markdown
# st.markdown('Markdown - Meenal Sharma markdown text')        #p
# st.markdown('# Meenal')        #h1
# st.markdown('## Meenal')        #h2
# st.markdown('### Meenal')        #h3
# st.markdown('#### Meenal')        #h4
# st.markdown('##### Meenal')        #h5
#
# st.markdown('*Meenal* is the developer')    # Italic
# st.markdown('_Meenal_ is the developer')    # Italic
# st.markdown('***Meenal*** is the developer')  # Italic + Bold
# st.markdown('***Meenal is the developer***')  # Italic + Bold
# st.markdown('**Meenal** is the developer')    # Bold
# st.markdown('__Meenal__ is the developer')    # Bold
# st.markdown('___Meenal is the developer___')
#
# st.markdown('1. first point')
# st.markdown('2. Second point')
# st.markdown('''3. third point
#                4. forth point''')
# st.markdown('- third point')
# st.markdown('- forth point')
#
# st.write('Text is here')
# st.write(range(1,10))

# ***********************************************************************************
# # INPUT TAGS
# st.subheader('1. Text input')
# name = st.text_input('Enter your name : ', value = 'First Last')
# st.write('Hello', name)
#
# st.subheader('2. Text area')
# st.text_area('Tell me something about yourself in 200 words', height = 200, max_chars = 500, help = 'Maximum 500 characters allowed')
#
# st.subheader('3. Password')
# st.text_input('Enter the password', type = 'password',help = 'Min 8 characters')
#
# st.subheader('4. Numeric input')
# st.number_input('Enter the age : ', min_value = 18, max_value = 34, step = 1, value = 24)
#
# st.subheader('5. Date input')
# today = datetime.now().date()
# date = st.date_input('Enter the date : ', value = today, min_value = today, max_value = today.replace(year = today.year + 1))
# st.write("You've selected : ", datetime.strftime(date, '%m/%d/%y'))
#
# ***********************************************************************************
# # BUTTONS
# st.subheader('1. Radio Button')
# gender = st.radio('Select gender : ', options = ('Male', 'Female', 'Other'), help = 'Choose One', horizontal = True)
# st.write("You've selected", gender)
#
# st.subheader('2. Select Box')
# option = st.selectbox('Select your options : ', options = ('Data Analysis','ML',"DL",'AI'), help = 'Choose One')
#
# st.subheader('3. MultiSelect Box')
# options = st.multiselect('Select your options : ', options = ('Data Analysis','ML',"DL",'AI'), help = 'Choose One', default = 'Data Analysis')
#
# st.subheader('4. Button')
# if st.button('Say Hello'):
#     st.write('Hi')
#
# st.subheader('5. Color Picker')
# color = st.color_picker('Select your fav color : ', '#D63053')
# st.write("You've selected the color" , color)
#
# st.subheader('6. Checkbox')
# if st.checkbox('I agree to T&C.', help = 'You must agree'):
#     st.write('thanks for agreeing')
#
# st.button('Submit your application')

# ***********************************************************************************
# # FORMS
# st.title('BMI  Calculator')
#
# with st.form('BMI  Calculator'):
#     col1, col2, col3 = st.columns([2,2,1])
#
# with col1:
#     weight = st.number_input('Enter your weight in KGs')
#
# with col2:
#     height = st.number_input('Enter your height in Meters')
#
# with col3:
#     submit = st.form_submit_button('Calculate')
#
# if submit:
#     BMI = round(weight / (height**2), 2)
#     st.write("Your BMI =", BMI)
#     if BMI <= 18.5:
#         st.error('Underweight')
#     elif BMI > 18.5 and BMI <= 24.9:
#         st.success('Healthy / Normal')
#     elif BMI > 25 and BMI <= 29.9:
#         st.warning('Overweight')
#     else:
#         st.error('OBESE')

# ***********************************************************************************
# # SCRIPTS
# def rate_yourelf():
#     with st.sidebar:
#         st.title('Rate Yourself')
#         languages = st.text_input('Enter the programming languages you know with comma separation', value = 'Python')
#         languages = [i.strip() for i in languages.split(',')]
#
#     st.subheader('How would you rate your experience in the following programming languages and tools?')
#
#     for lang in languages:
#         st.write(lang)
#         st.slider(lang, min_value = 0. , max_value = 10. , step = .5 )
#
# def bmi_calculator():
#     st.title('BMI  Calculator')
#
#     with st.form('BMI  Calculator'):
#         col1, col2, col3 = st.columns([2,2,1])
#
#     with col1:
#         weight = st.number_input('Enter your weight in KGs')
#
#     with col2:
#         height = st.number_input('Enter your height in Meters')
#
#     with col3:
#         submit = st.form_submit_button('Calculate')
#
#     if submit:
#         BMI = round(weight / (height**2), 2)
#         st.write("Your BMI =", BMI)
#         if BMI <= 18.5:
#             st.error('Underweight')
#         elif BMI > 18.5 and BMI <= 24.9:
#             st.success('Healthy / Normal')
#         elif BMI > 25 and BMI <= 29.9:
#             st.warning('Overweight')
#         else:
#             st.error('OBESE')
#
#
# choice = st.sidebar.selectbox('Menu', ['BMI', 'Rate Yourself'])
#
# if choice == 'BMI':
#     bmi_calculator()
#
# elif choice == 'Rate Yourself':
#     rate_yourelf()


# ***********************************************************************************
# # IMAGES
# import time
# import numpy as np
#
# #Static
# col1,col2,col3 = st.columns(3)
#
# with col1:
#     st.header('Cat')
#     st.image('https://static.streamlit.io/examples/cat.jpg', width = 200)
# with col2:
#     st.header('Dog')
#     st.image('https://static.streamlit.io/examples/dog.jpg', width = 200)
# with col3:
#     st.header('Owl')
#     st.image('https://static.streamlit.io/examples/owl.jpg', width = 200)
#
# #Dynamic
# n = st.number_input('How many columns do you want?', 1,10)
# cols = st.columns(n)
# for col in cols:
#     with col:
#         st.image('https://static.streamlit.io/examples/cat.jpg')

# ***********************************************************************************

# # TABS
# import time
# import numpy as np
# import pandas as pd
#
# # Static
# tab1, tab2, tab3 = st.tabs(['Cat', 'Dog','Owl'])
# tab1.image('https://static.streamlit.io/examples/cat.jpg', width = 200)
# tab2.image('https://static.streamlit.io/examples/dog.jpg', width = 200)
# tab3.image('https://static.streamlit.io/examples/owl.jpg', width = 200)
#
# # Dynamic
# imgs = pd.read_csv('/Users/user/Streamlit/imgs.csv')['img_link']
#
# tabs = st.tabs(["ID"]*30)
# for tab in tabs:
#     img = imgs[np.random.randint(1,1000)]
#     tab.image(img, width = 400)
# # st.subheader(imgs)

# ***********************************************************************************

# # EXPANDERS & EMPTY FUNCTIONALITY
# import numpy as np
# import pandas as pd
# import time

# cases = []
# for _ in range(36):
#     cases.append(np.random.randint(1,7))
#
# data = []
# for i in range(1,7):
#     data.append(cases.count(i))
#
# st.header('Frequency of getting a face')
#
# st.bar_chart({'data': data})
#
# with st.expander('See Explanation'):
#     st.write('''
#         The chart shows some numbers I got from rolling a dice 100times
#         and its basically about how many imes each face appears
#         ''')
#     st.image("https://static.streamlit.io/examples/dice.jpg")

# with st.empty():
#     st.write('You need to wait for 10 seconds')
#     for seconds in range(11):
#         st.write('⌛' +str(seconds) + ' seconds remaining')
#         time.sleep(1)
#     st.write('10 seconds completed')

# ***********************************************************************************

# # PROGRESS BARS & ADVANCE options
# import time
#
# st.set_page_config(page_title = 'Streamlit practice', page_icon = '🥳', layout = 'wide')
#
# # Spinner
# with st.spinner('Wait for it'):
#     time.sleep(2)
#     st.write('Thanks for your patience!')
#
# # Progress bars
# with st.empty():
#     for percent_completed in range(10):
#         time.sleep(.1)
#         st.progress(percent_completed + 1, text = 'Processing')
#     st.success('Process completed')
#
# st.balloons()
#
# st.snow()

# ***********************************************************************************
# # ECHO & STOP
# import time
# # st.write('This is a code sample')
# # st.code('This is a code sample')
# # st.code("st.write('This is a code sample')")
#
# def get_user():
#     return ' Meenal'
#
# with st.echo():
#     def get_punc():
#         return '!!!'
#
#     greeting = 'Hi there, '
#     name = get_user()
#     punc = get_punc()
#     st.write(greeting, name, punc)
#
# #  STOP
# f_name = st.text_input('Enter first name : ')
# if not f_name:
#     st.warning('No name entered')
#     st.stop()
#
# l_name = st.text_input('Enter last name : ')
# if not l_name:
#     st.warning('No name entered')
#     st.stop()
#
# st.success('Thank you for entering your name')

# ***********************************************************************************
# MEDIA FILES

# # IMAGE
# st.title('1. Image from Path')
# img = Image.open('/Users/user/Streamlit/daisy-flower.jpeg')
# st.image(img)

# st.title('2.Image from Link')
# st.image('https://media.geeksforgeeks.org/gfg-gg-logo.svg', width = 500)
#
# # VIDEO
# st.title('3. Video')
# video_file = open('/Users/user/Streamlit/2616637-hd_1920_1080_30fps.mp4', 'rb')
# st.video(video_file)
#
# # AUDIO
# st.title('4. Audio')
# audio_file = open('/Users/user/Streamlit/heavy-rain-thunder-145345.mp3', 'rb')
# st.audio(audio_file.read())

# ***********************************************************************************
# DATAFRAMES
# import pandas as pd

# df = pd.read_csv('')
# st.subheader('1. Displaying the entire dataframe')
# st.dataframe(df)
#
# st.subheader('2. Displaying the head of dataframe')
# st.dataframe(df.head())
#
# st.subheader('3. Displaying the tail of dataframe')
# st.dataframe(df.tail())
#
# st.title('4. Displaying in a Table (first 20 rows)')
# st.dataframe(df.head(20))

# st.title('5. Displaying JSON')
#
# js = [{'p_id' : 1, 'name' : '5 Star'},
#       {'p_id' : 2, 'name' : 'Milku Bar'},
#       {'p_id' : 3, 'name' : 'Kit Kat'},
#       {'p_id' : 4, 'name' : 'Perk'},
#       {'p_id' : 5, 'name' : 'Munch'}]
#
# st.json(js)
#
# st.title('6. Displaying the description of Data')
# st.table(df.describe())

# ***********************************************************************************
# UPLOAD FILES
st.title('File Uploading')

# Image
st.subheader('1. Uploading Image')
img_file = st.file_uploader('Upload Image', type = ['png', 'jpg','jpeg'])
if img_file is not None:

    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type, 'file_size':img_file.size}
    st.write(file_details)

    st.image(Image.open(img_file))
# Audio
st.subheader('2. Uploading Audio')
audio_file = st.file_uploader('Upload Audio File', type = ['wav', 'mp3'])
if audio_file is not None:
    file_details = {'file_name' : audio_file.name,
                    'file_type' : audio_file.type,
                    'file_size' : audio_file.size}
    # st.write(audio_file)
    st.audio(audio_file)
# Video
st.subheader('2. Uploading Video')
video_file = st.file_uploader('Upload Video File', type = ['mp4', 'mov'])
if video_file is not None:
#     file_details = {'file_name' : video_file.name,
#                     'file_type' : video_file.type,
#                     'file_size' : video_file.size}
    # st.write(audio_file)
    st.video(video_file) 

# ***********************************************************************************
#
# # IMAGE CONVERTER
# from PIL import Image
#
# def convert_img(image_path, new_format):
#     with Image.open(image_path) as img:
#
#         new_name = image_path.name.split('.')[0] + '.' + new_format
#         final_path = '/Users/user/Streamlit/' + new_name
#
#         img = img.convert('RGB')
#
#         st.subheader(final_path)
#         img.save(final_path)
#         st.success('Image Saved at '+ final_path)
#
#
# st.title('Image Converter')
# img_file = st.file_uploader('Upload Your Image', type = ['png','jpeg','jpg'])
#
# new_format = st.selectbox('Select the output format', ['png','jpeg','jpg'])
#
# if st.button('Convert'):
#     if img_file is not None:
#         convert_img(img_file, new_format)
#     else:
#         st.error('Please upload the img file')

# ***********************************************************************************
# # Image Rotation
# from PIL import Image
# import cv2 as cv
# import numpy as np
#
# def rotate_img(image, angle):
#     img = np.array(image)
#     height, width = img.shape[:2]
#     M = cv.getRotationMatrix2D((width/2, height/2), angle, 1)
#     rotated_img = cv.wrapAffine(img, M, (width, height))
#     return rotated_img
#
# st.title('Image Rotator')
# st.subheader('Upload the image: ')
# img_file = st.file_uploader('Upload your image', type = ['png','jpg','jpeg'])
#
# st.subheader('Rotate the image:')
# angle = st.slider('Select Angle: ', -180,180,0,1)
#
# if img_file is not None:
#     image = Image.open(img_file)
#     rotated_img = rotate_img(image, angle)
#     st.image(rotated_img)
# else:
#     st.write('Image not uploaded.')

# ***********************************************************************************
# #PLOTS
# st.title('Line Chart')
# chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['L-1','L-2','L-3'])
# st.line_chart(chart_data)
#
# st.title('Area Chart')
# st.area_chart(chart_data)
#
# st.title('Bar Chart')
# st.bar_chart(chart_data)

# ***********************************************************************************
# # Plots with seaborn
# st.subheader('Data Visualization with Seaborn and Matplotlib')
#
# st.text('Displaying the dataset')
# df = pd.read_csv('/Users/user/Downloads/iris.csv')
# st.dataframe(df)
#
# st.text('Barplot using Matplotlib')
# fig = plt.figure(figsize = (15,8))
# df['species'].value_counts().plot(kind = 'bar')
# st.pyplot(fig)
#
# st.text('Plot with Seaborn')
# fig = plt.figure(figsize = (15,8))
# sns.distplot(df['sepal_length'])
# st.pyplot(fig)
#
# st.text('Displaying Multiple Graphs')
# col1,col2 = st.columns(2)
# with col1:
#     col1.write('KDE = False')
#     fig1 = plt.figure()
#     sns.distplot(df['sepal_length'], kde = False)
#     st.pyplot(fig1)
# with col2:
#     col2.write('Hist = False')
#     fig2 = plt.figure()
#     sns.distplot(df['sepal_length'], hist = False)
#     st.pyplot(fig2)
#
#
# st.text('Changing the style of graphs')
# col1,col2 = st.columns(2)
# with col1:
#     fig1 = plt.figure()
#     sns.set_style('darkgrid')
#     sns.set_context('notebook')
#     sns.distplot(df['petal_length'], hist = False)
#     st.pyplot(fig1)
# with col2:
#     fig2 = plt.figure()
#     sns.set_theme('poster', style = 'darkgrid')
#     sns.distplot(df['petal_length'], hist = False)
#     st.pyplot(fig2)
#
# st.text('Scatter Plot')
# fig, ax = plt.subplots(figsize = (15,8))
# ax.scatter(*np.random.random(size = (2,1000)))
# st.pyplot(fig)
#
# st.text('Count Plot')
# fig = plt.figure(figsize = (15,8))
# sns.countplot(data = df, x = 'species')
# st.pyplot(fig)
#
# st.text('Box Plot')
# fig = plt.figure(figsize = (15,8))
# sns.boxplot(data = df, x='species', y='petal_length')
# st.pyplot(fig)
#
# st.text('Violin Plot')
# fig = plt.figure(figsize = (15,8))
# sns.violinplot(data = df, x='species', y='petal_length')
# st.pyplot(fig)

# ***********************************************************************************
# # PLOTLY Visualization
# st.title('Visualization with Plotly')
# df = pd.read_csv('/Users/user/Downloads/tips.csv')
# st.dataframe(df)
#
# st.text('1. Pie Chart')
# fig = px.pie(df, values = 'total_bill', names = 'day')
# st.plotly_chart(fig)
#
# st.text('2. Pie Chart (Donut Chart)')
# fig = px.pie(df, values = 'total_bill', names = 'day', opacity = .8, hole=.5,
# color_discrete_sequence = px.colors.sequential.RdBu)
# st.plotly_chart(fig)
#
# st.text('4. Multiple Distplots')
# x1 = np.random.randn(200) + 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) - 2
# hist_data = [x1,x2,x3]
# group_lbls = ['G1','G2', 'G3']
# fig = ff.create_distplot(hist_data, group_lbls)
# st.plotly_chart(fig, use_container_width=True)
