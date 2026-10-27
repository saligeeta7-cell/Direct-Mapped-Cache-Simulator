class DirectMappedCache:
    def __init__(self, cache_size_bytes, block_size_bytes):
        self.cache_size = cache_size_bytes
        self.block_size = block_size_bytes
        self.num_blocks = cache_size_bytes // block_size_bytes
        
        # Initialize cache lines (storing tags, valid bit set to False initially)
        self.cache = {i: {"valid": False, "tag": None} for i in range(self.num_blocks)}
        
        self.hits = 0
        self.misses = 0

    def access_memory(self, address):
        # Determine block index and tag
        block_index = (address // self.block_size) % self.num_blocks
        tag = address // self.cache_size
        
        cache_line = self.cache[block_index]
        
        if cache_line["valid"] and cache_line["tag"] == tag:
            status = "HIT"
            self.hits += 1
        else:
            status = "MISS"
            self.misses += 1
            # Update cache line on miss
            cache_line["valid"] = True
            cache_line["tag"] = tag
            
        print(f"Address: {address:3d} | Index: {block_index} | Tag: {tag} | Result: {status}")

    def get_statistics(self):
        total = self.hits + self.misses
        hit_rate = (self.hits / total) * 100 if total > 0 else 0
        print("\n--- Cache Performance Statistics ---")
        print(f"Total Accesses : {total}")
        print(f"Total Hits     : {self.hits}")
        print(f"Total Misses   : {self.misses}")
        print(f"Hit Rate       : {hit_rate:.2f}%")

if __name__ == "__main__":
    # Cache Configuration: 32 bytes total size, 4 bytes per block (8 blocks total)
    sim = DirectMappedCache(cache_size_bytes=32, block_size_bytes=4)
    
    # Sequence of memory addresses accessed by the CPU
    memory_trace = [2, 4, 2, 8, 5, 2, 20, 4, 8]
    
    print("--- Simulating Memory Accesses ---")
    for addr in memory_trace:
        sim.access_memory(addr)
        
    sim.get_statistics()
