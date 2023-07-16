
#start the application - this needs to be a loop through the cluster members
appManager=AdminControl.queryNames('cell=ip-172-31-17-69Cell01,node=ip-172-31-17-69Node01,type=ApplicationManager,process=liferay-member1,*')
AdminControl.invoke(appManager, 'startApplication', 'liferay-ce-yeti')