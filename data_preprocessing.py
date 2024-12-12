import pandas as pd
import os

'''负责读取CSV数据、生成视频路径并保存'''

def preprocess_data(raw_video_path, test_csv_path, sample_num=1000):
    test_df = pd.read_csv(test_csv_path)
    sample_df = test_df.sample(sample_num, random_state=42)
    sample_df['video_path'] = sample_df.apply(lambda x: os.path.join(raw_video_path, x['video_id']) + '.mp4', axis=1)
    sample_df.to_csv('./MSRVTT_JSFUSION_test_sample.csv')
    
    return sample_df

if __name__ == "__main__":
    raw_video_path = 'D:/Program/work/text_video_retrieval/data/test_1k_compress'
    test_csv_path = 'D:/Program/work/text_video_retrieval/data/MSRVTT_JSFUSION_test.csv'
    preprocess_data(raw_video_path, test_csv_path)
