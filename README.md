<h1>money-tracker</h1>

در این پروژه به بررسی و تست بخش Currencies وب اپلیکیشن money-tracker پرداختیم که کاربرد آن تبدیل واحد پولی کشور های مختلف به یکدیگر است. 
در این بخش یک dropdown وجود دارد که برای انتخاب واحد پول پایه به کار می رود. همچنین یک dropdown دیگر نیز وجود دارد که برای مشخص کردن کشور هایی به کار می رود که قصد داریم واحد پول کشور پایه را به واحد پول این کشور ها تبدیل کنیم.
در نهایت پس از انتخاب کشور های مورد نظر نتیجه تحت عنوان یک جدول نمایش داده می شود.
ما برای این پروژه دو تست نوشته ایم که در ادامه هر یک را توضیح داده ایم. 
<br></br>

![alt text](https://github.com/saleh-sh/money-tracker-Tests/blob/master/Screenshot.png?raw=true)

<h2>Tests</h2>
تست اول: این تست بررسی می کند که کشور هایی که در جدول نتیجه نشان داده می شود همان کشور هایی است که کاربر انتخاب کرده است یا خیر.  
تست دوم: کشور هدف (کشوری که در dropdwon دوم انتخاب می شود) نمی تواند تکراری باشد. در واقع در این برنامه می توان چند کشور را از dropdown دوم انتخاب کرد ولی هر کشور می تواند فقط یک بار انتخاب شود و پس از اینکه انتخاب شد دیگر نباید نمایش داده شود. تست دوم این مورد را چک می کند. یعنی بررسی می کند که کشوری که یک بار انتخاب شده باز هم به کاربر نمایش داده می شود یا خیر.

لینک پروژه: https://github.com/ayastreb/money-tracker
