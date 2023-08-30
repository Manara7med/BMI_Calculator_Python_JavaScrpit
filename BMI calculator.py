#Pyhon code
print("##################################################")
print("Welcome to the BMI calculator.")
height=float(input("Please Enter your height in meters:"))
weight=float(input("Please Enter your weight in kg:"))
print("##################################################")

def calculator_bmi(height,weight):
    bmi= weight /(height**2)
    return bmi

def interpret_bmi(bmi):
    if bmi <18.5:
        return "You Are Underweight"
    elif  18.5 < bmi < 25:
        return "You Weight is Normal"
    elif 25 < bmi < 30:
        return "You Are Overweight"
    else :
        return "You Are Obese"
    
bmi = calculator_bmi(height,weight)
interpretation = interpret_bmi(bmi)

result = f"Your BMI Value is:{bmi}\nInterpretation:{interpretation}"
print(result)





#Java Script code
alert("Welcome to the BMI calculator.");
var height=prompt("Please Enter your height in meters:");
var weight=prompt("Please Enter your weight in kg:");


function calculator_bmi(height,weight)
{
   var  bmi= weight /(height**2)
    return bmi
 }

function interpret_bmi(bmi)
{
    if (bmi <18.5)
        {
        return "You Are Underweight"}
    else if ( 18.5 < bmi < 25){
        return "You Weight is Normal"}
    else if (25 < bmi < 30){
        return "You Are Overweight"}
    else 
        {
        return "You Are Obese"}
}
var bmi = calculator_bmi(height,weight)
var interpretation = interpret_bmi(bmi)
console.log('Your BMI Value is:' + bmi);
console.log('Interpretation ' + interpretation);
