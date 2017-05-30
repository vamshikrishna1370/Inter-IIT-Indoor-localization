trap 'kill %1;' SIGINT
python vvamshi.py &
python finfun.py  
return 0

