% Converting Steim1 format Data from a Centaur to an Ascii file
% The Year, Month and Day have to be adapted, as well as the file Path
Year = '2023';%'2023';%
Month = '02';%'01','02';%
Day = {'14'};% {'07'};%
Channel = {'X','Y','Z'};
MeasurementName= '221223_longtermmeasurement';%'AccComparison';%
for d=0:23
    Hour{d+1} = num2str(d,'%02.f');
end
for k = 1:length(Channel)
    X=['start Channel ',Channel(k)];
    disp(X)
    Timeall = [];
    Accall  = [];
    for d = 1:length(Day)
        X=['start Day ',Day(d)];
        disp(X)
        for j = 1:length(Hour)
            X=['check Hour ',Hour(j)];
            disp(X)
            % here the filename has to be adapted for the Channel you choose
            FilePath = ['D:\data_collection\2-14-23\Seismometer data\Data'];
            SavePath = ['D:\data_collection\2-14-23\Seismometer data\Data'];
            %             if exist(FilePath)~= 0 && exist(SavePath)==0
%             X=['load File ',FilePath(end-13-44:end-13)];
            disp(X);
            A=rdmseed('D:\data_collection\2-14-23\Seismometer data\Data\XX.S0001..HHZ_centaur-6_8725_20230217_080000.miniseed');
            %%
            Time=[];
            Acc=[];
            X='write data to Time and Acc';
            disp(X)
            for i=1:size(A,2)
                temp = A(i).t;
                Time = [Time ; temp];
                temp = A(i).d;
                Acc = [Acc ; temp];
            end
            SavePath=['D:\data_collection\2-14-23\Seismometer data\Data\','XX.S0001..HHZ_centaur-6_8725_20230217_080000.txt'];
            fileID=fopen(SavePath,'w');
            M = [transpose(Time); transpose(Acc)];
            fprintf(fileID,'%7s %6s\n', 'Time','Acc');
            fprintf(fileID,'%7.11f %6.1f\n', M);
            fclose(fileID);
            Timeall = [Timeall ; Time];
            Accall = [Accall ; Acc];
            %             end
        end
    end
    % when a file for all channel during the whole duration should be
    % generated uncomment the following lines, but notice, that files can
    % get really large and fill your whole RAM:
    %     SavePath = ['D:\Data\',Year,'\',Month,'\',MeasurementName,'\Acc2\Channel',Channel{k},'.txt'];
    %     fileID=fopen(SavePath,'w');
    %     M = [transpose(Timeall); transpose(Accall)];
    %     fprintf(fileID,'%7s %6s\n', 'Time','Acc');
    %     fprintf(fileID,'%7.11f %6.1f\n', M);
    %     fclose(fileID);
end
disp('finish');