#!/bin/bash

url="https://www.khanacademy.org/api/v1/topic/"
first_topic='arithmetic'
url=$url$first_topic
echo $url
echo " "
echo " "
sleep 5s
curl $url > khan.json
python khan_academy.py
echo " "
echo " "



for i in {0..51}
do
url="https://www.khanacademy.org/api/v1/topic/"
array=('pre-algebra' 'early-math' 'algebra' 'geometry' 'trigonometry' 'precalculus' 
	'statistics-probability' 'ap-calculus-ab' 'ap-calculus-bc' 'multivariable-calculus' 
	'differential-calculus' 'linear-algebra' 'cc-kindergarten-math' 'cc-1st-grade-math' 
	'cc-2nd-grade-math' 'cc-third-grade-math' 'cc-fourth-grade-math' 'cc-fifth-grade-math' 
	'cc-sixth-grade-math' 'cc-seventh-grade-math' 'cc-eighth-grade-math' 'engageny' 
	'math-1-2-3' 'biology' 'physics' 'chemistry' 'cosmology-and-astronomy' 'health-and-medicine' 
	'electrical-engineering' 'organic-chemistry' 'ap-physics-1' 'ap-physics-2' 'ap-chemistry' 
	'ap-biology' 'computing' 'computer-programming' 'computer-science' 'hour-of-code' 'world-history' 
	'us-history' 'ap-us-history' 'art-history' 'grammar' 'microeconomics' 'macroeconomics' 
	'core-finance' 'entrepreneurship2' 'sat' 'mcat' 'nclex-rn' 'gmat' 'iit-jee-subject')
url=$url${array[i]}
echo $url
echo " "
echo " "
sleep 5s
curl $url > khan.json
python khan_academy_noheaders.py
echo " "
echo " "
done

exit 0