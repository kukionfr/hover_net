import os
from time import time

src = r"\\10.162.80.17\Kyu\Research\Database\Skin_Aging_Complete_Rescan\wsi"
cachedir = r"C:\Users\kyuha\Desktop\cache"
start = time()
dst = os.path.join(src,'hovernet_out')
# nr_inference_workers 0 if fails
os.system('python run_infer.py '\
          '--nr_types={} '\
          '--batch_size={} '\
          '--nr_inference_workers={} '\
          '--nr_post_proc_workers={} '\
          '--model_mode={} '\
          '--model_path={} '\
          'wsi '\
          '--input_dir="{}" '\
          '--output_dir="{}" '\
          '--proc_mag={} '\
          '--cache_path={} '\
          '--save_thumb --save_mask'\
          .format(0,16,8,11,'original',
                  "./models/pretrained/hovernet_original_consep_notype_tf2pytorch.tar",
                  src,
                  dst,
                  20,
                  cachedir,
                  )
          )
end = time()
print('execution time : ',end-start)

