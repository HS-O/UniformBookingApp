from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/male', methods=['GET', 'POST'])
def show_male():
  if request.method == 'GET':
    return render_template('show_male.html')
  else:
    #if request.form.get('submit'):
    school = request.form.get('school')
    level = request.form.get('level')
    name = request.form.get('name')
    phone = request.form.get('phone')
    Class = request.form.get('Class')
    data_list =[]
    data_list += [school, level, name, phone, Class]
    final_data = ''
    final_data += school + ' ' + level + ' ' + name + ' ' + phone + ' ' + Class
    with open('data1.txt', 'a') as _file:
      _file.write(final_data)
    _file.close
    return render_template("booking_male.html",  school=school, level=level, name=name, phone=phone, Class=Class)

@app.route('/female', methods=['GET', 'POST'])
def show_female():
  if request.method == 'GET':
    return render_template('show_female.html')
  else: #submit button??
    school1 = request.form.get('school1')
    level1 = request.form.get('level1')
    name1 = request.form.get('name1')
    phone1 = request.form.get('phone1')
    Class1 = request.form.get('Class1')
    data_list1 =[]
    data_list1 += [school1, level1, name1, phone1, Class1]
    final_data1 = ''
    final_data1 += school1 + ' ' + level1 + ' ' + name1 + ' ' + phone1 + ' ' + Class1
    with open('data2.txt', 'a') as _file:
      _file.write(final_data1)
    _file.close
    return render_template("booking_female.html",  school1=school1, level1=level1, name1=name1, Class1=Class1, phone1=phone1,)
  
@app.route('/booking_male', methods=['GET', 'POST'])
def booking_male():
  if request.method == 'GET':
    return render_template('booking_male.html')
  else:
    total_amt = 0
    quantity_1 = int(request.form.get('quantity_1'))
    quantity_2 = int(request.form.get('quantity_2'))
    quantity_3 = int(request.form.get('quantity_3'))
    quantity_4 = int(request.form.get('quantity_4'))
    total_amt = 9 * quantity_1 + 9 * quantity_2 + 9 * quantity_3 + 9 * quantity_4
    size4 = request.form.get('size4')
    if size4 is None:
      size4 = ''
    size5 = request.form.get('size5')
    if size5 is None:
      size5 = ''
    size6 = request.form.get('size6')
    if size6 is None:
      size6 = ''
    size7 = request.form.get('size7')
    if size7 is None:
      size7 = ''
    data_list2 =[]
    data_list2 += [size4, quantity_1, size5, quantity_2, size6, quantity_3, size7, quantity_4] 
    final_data2 = '' 
    final_data2 += size4 + ' ' + str(quantity_1) + ' ' + size5 + ' ' + str(quantity_2) + ' ' + size6 + ' ' + str(quantity_3) + ' ' + size7 + ' ' + str(quantity_4)
    with open('size1.txt', 'a') as _file:
      _file.write(final_data2)
    return render_template('booking_male.html', total_amt=total_amt, quantity_1=quantity_1, quantity_2=quantity_2, quantity_3=quantity_3,  quantity_4=quantity_4, size4=size4, size5=size5, size6=size6, size7=size7)

@app.route('/booking_female', methods=['GET', 'POST'])
def booking_female():
  if request.method == 'GET':
    return render_template('booking_female.html')
  else:
    total_amt1 = 0
    quantity_5 = int(request.form.get('quantity_5'))
    quantity_6 = int(request.form.get('quantity_6'))
    quantity_7 = int(request.form.get('quantity_7'))
    quantity_8 = int(request.form.get('quantity_8'))
    total_amt1 = 9 * quantity_5 + 9 * quantity_6 + 9 * quantity_7 + 9 * quantity_8
    size = request.form.get('size')
    if size is None:
      size = ''
    size1 = request.form.get('size1')
    if size1 is None:
      size1 = ''
    size2 = request.form.get('size2')
    if size2 is None:
      size2 = ''
    size3 = request.form.get('size3')
    if size3 is None:
      size3 = ''
    data_list3 =[]
    data_list3 += [size, quantity_5, size1, quantity_6, size2, quantity_7, size3, quantity_8] 
    final_data3 = '' 
    final_data3 += size + ' ' + str(quantity_5) + ' ' + size1 + ' ' + str(quantity_6) + ' ' + size2 + ' ' + str(quantity_7) + ' ' + size3 + ' ' + str(quantity_8)
    with open('size2.txt', 'a') as _file:
      _file.write(final_data3)
    return render_template('booking_female.html', total_amt1=total_amt1, quantity_5=quantity_5, quantity_6=quantity_6, quantity_7=quantity_7,  quantity_8=quantity_8, size=size, size1=size1, size2=size2, size3=size3)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
  if request.method == 'GET':
    return render_template('payment.html')
  else:
    return render_template('final.html')

@app.route('/final', methods=['GET', 'POST'])
def final():
  if request.method == 'GET':
    return render_template('final.html')
  else:
    return render_template('index.html')
 
@app.route('/easter_egg', methods=['GET', 'POST'])
def easter_egg():
  if request.method == 'GET':
    return render_template('easter_egg.html')
  else:
    return render_template('index.html')
app.run(host='0.0.0.0', port=8080)