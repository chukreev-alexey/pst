ifeq ($(MIN),True)
	ARGV=--production
endif

build:
	gulp clean
	gulp bower
	gulp css $(ARGV)
	gulp images $(ARGV)
	gulp webpack $(ARGV)
	make email

min:
	gulp css --prod
	gulp webpack --prod

release:
	gulp bump
	git commit -am "Bumped version"
	gulp tag
	git push origin master --tags
	echo "Release finished"

gulptasks:
	rm -rf ./gulp-tasks
	git archive --remote=git@bitbucket.org:itcase-dev/gulp-tasks.git master gulp-tasks/* gulpfile.js gulpfile.paths.js __gulpfile.local.js | tar -xv
	mv __gulpfile.local.js ./defaults/__gulpfile.local.js

webpackconfig:
	git archive --remote=git@bitbucket.org:itcase-dev/gulp-tasks.git master webpack.config.dev.js webpack.config.prod.js | tar -xv

loadrc:
	git archive --remote=git@bitbucket.org:itcase-dev/gulp-tasks.git master .babelrc .browserslistrc .eslintignore .eslintrc .htmlhintrc .huskyrc .lintstagedrc .lintstagedrc .prettierignore .prettierrc .stylelintrc | tar -xv

email:
	gulp emailTemplates --path templates/emails/ $(ARGV)
	gulp emailTemplates --path templates/itcase_cart/emails/ $(ARGV)
	gulp emailTemplates --path templates/itcase_entry/emails/ $(ARGV)

font:
	gulp font -F Fact-Regular -N 'Fact' -W normal
	gulp font -F Fact-Medium -N 'Fact' -W 500
	gulp font -F Fact-Bold -N 'Fact' -W bold
	gulp font -F Fact-Expanded -N 'Fact-Expanded' -W normal
	gulp font -F Fact-ExpandedBold -N 'Fact-Expanded' -W bold
	gulp font -F Fact-SemiExpanded -N 'Fact-Semi-Expanded' -W normal
	gulp font -F Fact-SemiExpandedMedium -N 'Fact-Semi-Expanded' -W 500
	gulp font -F Fact-SemiExpandedBold -N 'Fact-Semi-Expanded' -W bold

MEDIA_PATH=media/uploads/

DEV_PROJECT=pst
DEV_DB=pst
DEV_SERVER=web@193.107.238.41
DEV_SERVER_MEDIA=~/$(DEV_PROJECT)/src/$(MEDIA_PATH)
DEV_DUMP=~/$(DEV_PROJECT)/$(DEV_PROJECT).sql
DEV_DB_PASS="94hXvvdwFSaX5qicSDwR"

LOCAL_PROJECT=pst
LOCAL_DB=pst
LOCAL_SERVER=itcase@192.168.1.21
LOCAL_DUMP=~/$(LOCAL_PROJECT).sql
LOCAL_DB_PASS="94hXvvdwFSaX5qicSDwR"

PROD_PROJECT=pst
PROD_DB=pst
PROD_SERVER=web@213.189.220.212
PROD_SERVER_MEDIA=~/$(PROD_PROJECT)/src/$(MEDIA_PATH)
PROD_DUMP=~/$(PROD_PROJECT)/$(PROD_PROJECT).sql


dev-uploadimages:
	rsync -ahvz --exclude '.DS_Store' $(MEDIA_PATH) $(DEV_SERVER):$(DEV_SERVER_MEDIA)

dev-loadimages:
	rm -rf $(MEDIA_PATH)
	mkdir -p $(MEDIA_PATH)
	rsync -ahvz $(DEV_SERVER):$(DEV_SERVER_MEDIA) $(MEDIA_PATH)

dev-getdata:
	ssh -A $(DEV_SERVER) 'PGPASSWORD=$(DEV_DB_PASS) pg_dump -h localhost -U $(DEV_DB) -d $(DEV_DB) -f $(DEV_DUMP) -bcOv'
	scp $(DEV_SERVER):$(DEV_DUMP) ${CURDIR}
	ssh -A $(DEV_SERVER) 'rm $(DEV_DUMP)'
	scp $(DEV_PROJECT).sql $(LOCAL_SERVER):~/
	ssh $(LOCAL_SERVER) 'PGPASSWORD=$(LOCAL_DB_PASS) psql -h localhost -U $(LOCAL_DB) -d $(LOCAL_DB) -f ./$(DEV_PROJECT).sql'
	ssh -A $(LOCAL_SERVER) 'rm ./$(DEV_PROJECT).sql'
	rm ./$(DEV_PROJECT).sql

dev-uploaddata:
	ssh -A $(LOCAL_SERVER) 'PGPASSWORD=$(LOCAL_DB_PASS) pg_dump -h localhost -U $(LOCAL_DB) -d $(LOCAL_DB) -f $(LOCAL_DUMP) -bcOv'
	scp $(LOCAL_SERVER):$(LOCAL_DUMP) ${CURDIR}
	ssh -A $(LOCAL_SERVER) 'rm $(LOCAL_DUMP)'
	scp $(LOCAL_PROJECT).sql $(DEV_SERVER):~/
	ssh $(DEV_SERVER) 'PGPASSWORD=$(DEV_DB_PASS) psql -h localhost -U $(DEV_DB) -d $(DEV_DB) -f ./$(LOCAL_PROJECT).sql'
	ssh -A $(DEV_SERVER) 'rm ./$(LOCAL_PROJECT).sql'
	rm ./$(LOCAL_PROJECT).sql

prod-uploadimages:
	rsync -ahvz --exclude '.DS_Store' $(MEDIA_PATH) $(PROD_SERVER):$(PROD_SERVER_MEDIA)

prod-loadimages:
	rm -rf $(MEDIA_PATH)
	mkdir -p $(MEDIA_PATH)
	rsync -ahvz $(PROD_SERVER):$(PROD_SERVER_MEDIA) ./$(MEDIA_PATH)

prod-getdata:
	ssh -A $(PROD_SERVER) 'pg_dump -h localhost -U $(PROD_DB) -d $(PROD_DB) -f $(PROD_DUMP) -bcOv'
	scp $(PROD_SERVER):$(PROD_DUMP) ${CURDIR}
	ssh -A $(PROD_SERVER) 'rm $(PROD_DUMP)'
	scp $(PROD_PROJECT).sql $(LOCAL_SERVER):~/
	ssh $(LOCAL_SERVER) 'PGPASSWORD=$(LOCAL_DB_PASS) psql -h localhost -U $(LOCAL_DB) -d $(LOCAL_DB) -f ./$(PROD_PROJECT).sql'
	ssh -A $(LOCAL_SERVER) 'rm ./$(PROD_PROJECT).sql'
	rm ./$(PROD_PROJECT).sql

connectproddb:
	ssh -N -L 127.0.0.1:5432:localhost:5432 $(PROD_SERVER)
